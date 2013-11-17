import os, urllib
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from sibzy.api.models import *
from django.db.models import Q
import facebook, json
from django.contrib.auth import logout, login

class SibzyAuthenticationMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            request.user_profile = get_object_or_404(UserProfile, user=request.user.id)

# returns user_profile
def fb_me(request):
    if 'fbid' in request.COOKIES and 'fbaccess_token' in request.COOKIES:
        user_profile = UserProfile.objects.filter(facebook_id=request.COOKIES['fbid'], access_token=request.COOKIES['fbaccess_token'])
        if len(user_profile) > 0:
            user_profile = user_profile[0]
            me = facebook.GraphAPI(user_profile.access_token)
            me = me.get_object('me')
            me['access_token'] = user_profile.access_token
            me['fbid'] = me['id']
            me['id'] = user_profile.id
            return me
        else:
            return None

def auth_logout(request):
    response = HttpResponse(json.dumps({'status': 'success'}))
    response.set_cookie('fbaccess_token', '')
    response.set_cookie('fbid', '')
    logout()
    return response

def auth_fblogin(request):
    if get_user(request): return HttpResponseRedirect('/')

    if 'error' in request.GET or 'code' not in request.GET:
        return HttpResponse(json.dumps({'status': 'error'}))
    
    code = request.GET['code']
    access_token = facebook.get_access_token_from_code(code, 'http://www.sibzy.com/login/facebook', '259749734165537', '30894c0518e604fa530c7c36f21cdaea')['access_token']

    graph = facebook.GraphAPI(access_token)
    profile = graph.get_object('me')

    user_profile = UserProfile.objects.filter(facebook_id=profile['id'])
    if len(user) > 0:
        user_profile = user_profile[0]
        user_profile.fbaccess_token = access_token
        user_profile.fbusername = profile['username']
        user_profile.save()
    else:
        user = User.objects.create_user(profile['id'], profile['id'] + '@facebook.com', profile['id'] + 'sibzypassword')
        user.save()
        user_profile = UserProfile(user=user, fbid=profile['id'], fbaccess_token=access_token, fbusername=profile['username'])        
        user_profile.save()
        
    user = authenticate(username=profile['id'], password=profile['id'] + 'sibzypassword')
    if user is not None and user.is_active:
        login(request, user)
    else:
        return HttpResponse(json.dumps({'status': 'error'}))

    response = HttpResponse(json.dumps({'status': 'success'}))
    response.set_cookie('fbid', profile['id'])
    response.set_cookie('fbaccess_token', access_token)
    return response