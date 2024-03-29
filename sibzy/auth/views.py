import os, urllib
import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from auth.models import User, UserProfile
import facebook
import simplejson as json
from django.contrib.auth import logout, login, authenticate
from django.views.decorators.csrf import ensure_csrf_cookie


def userprofile_processor(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    if request.user.is_authenticated():
        return {
            'profile': UserProfile.objects.get(user=request.user.id)
        }
    else:
        return {}


@login_required
@ensure_csrf_cookie
def logout_user(request):
    ''' Logout from the django seesion. Delete the *fbaccess_token* and *fbid* cookie.

    **Returns:**
        ``{status: 'success'}``
    '''
    response = HttpResponseRedirect('/')
    response.set_cookie('fbaccess_token', '', expires='Thu, 01-Jan-1970 00:00:00 GMT')
    response.set_cookie('fbid', '', expires='Thu, 01-Jan-1970 00:00:00 GMT')
    logout(request)
    return response

@ensure_csrf_cookie
def me(request):
    return render(request, 'auth_me.html')


@login_required
@ensure_csrf_cookie
def me_noajax(request):
    return render(request, 'auth_me_noajax.html')


@login_required
@ensure_csrf_cookie
def me_save_noajax(request):
    vegetarian = int(request.POST['vegetarian'])
    vegan = int(request.POST['vegan'])
    organic = int(request.POST['organic'])
    nutfree = int(request.POST['nutfree'])
    glutenfree = int(request.POST['glutenfree'])
    if vegetarian in (-1, 0, 1) and vegan in (-1, 0, 1):
        profile = UserProfile.objects.get(user=request.user.id)
        profile.vegetarian = vegetarian
        profile.vegan = vegan
        profile.organic = organic
        profile.nutfree = nutfree
        profile.glutenfree = glutenfree
        profile.save()
    return HttpResponseRedirect('/auth/me')

#@login_required
#def logout_fb(request):
#    ''' Logout from the django seesion. Delete the *fbaccess_token* and *fbid* cookie.
#
#    **Returns:**
#        ``{status: 'success'}``
#    '''
#
#    response = HttpResponse(json.dumps({'status': 'success'}))
#    response.set_cookie('fbaccess_token', '', expires='Thu, 01-Jan-1970 00:00:00 GMT')
#    response.set_cookie('fbid', '', expires='Thu, 01-Jan-1970 00:00:00 GMT')
#    logout(request)
#    return response


@ensure_csrf_cookie
def login_fb(request):
    ''' Login the user in the django session.
    Also convert short lived token to long lived token and tell the client about the long lived token.
    Also save into our database the long lived token.

    This gets called using the short lived access token generated by the client API.

    **Returns:**
        *On Success*: ``{status: 'success', access_token: '<long lived access token>'}``

        *On Error*: ``{status: 'error', code: <integer error code>}``
    '''

    if request.user.is_authenticated() and 'fbid' in request.COOKIES:
        return HttpResponseRedirect('/')

    if 'error' in request.POST or 'access_token' not in request.POST:
        return HttpResponse(json.dumps({'status': 'error', 'code': 1}))

    ## Initialize graph using short lived access token
    short_access_token = request.POST['access_token']
    #graph = facebook.GraphAPI(short_access_token)
    #
    ## Attempt extending access token
    #graph_response = graph.extend_access_token('259749734165537', '30894c0518e604fa530c7c36f21cdaea')
    #
    #if 'access_token' not in graph_response:  # If failed
    #    return HttpResponse(json.dumps({'status': 'error', 'code': 2}))
    #
    #long_access_token = facebook.get_access_token_from_code(code, 'http://www.sibzy.com/login/facebook', '259749734165537',
    #                                                   '30894c0518e604fa530c7c36f21cdaea')['access_token']

    # For now let's not worry about expriation of access token and just use short lived token
    long_access_token = short_access_token

    graph = facebook.GraphAPI(long_access_token)
    profile = graph.get_object('me')
    if 'username' not in profile:
        profile['username'] = profile['id']
        
    print profile
    user = User.objects.filter(userprofile__fbid=profile['id'])

    if len(user) > 0:
        user = user[0]
        user_profile = user.userprofile
        user_profile.fbaccess_token = long_access_token
        user_profile.fbusername = profile['username']
        user_profile.save()
    else:
        print 'T'
        user = User.objects.create_user(profile['id'], profile['id'] + '@facebook.com', profile['id'] + 'sibzypassword')
        user.save()
        print '5'
        user_profile = UserProfile(user=user, fbid=profile['id'], fbaccess_token=long_access_token,
                                   fbusername=profile['username'])
        print '4'
        user_profile.save()
        user_profile = UserProfile.objects.filter()
        print user_profile

    user = authenticate(username=profile['id'], password=profile['id'] + 'sibzypassword')
    if user is not None and user.is_active:
        login(request, user)
    else:
        return HttpResponse(json.dumps({'status': 'error', 'code': 3}))

    response = HttpResponse(json.dumps({'status': 'success', 'access_token': long_access_token}))
    response.set_cookie('fbid', profile['id'])
    response.set_cookie('fbaccess_token', long_access_token)
    return response
