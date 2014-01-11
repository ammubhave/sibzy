import os, urllib
import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from auth.models import User, UserProfile
from comment.models import Comment, CommentVote
from restaurant.models import Dish
import json


@login_required
def comment_get(request, comment_id):
    ''' Get the comment with id = comment_id

    **Arguments:**
        *comment_id*: Comment ID

    **Returns:**
        ``<comment json object>``
    '''

    comment = get_object_or_404(Comment, id=comment_id)

    return HttpResponse(comment.json())


@login_required
def comment_set(request, comment_id):
    ''' Updates the comment with id = comment_id

    **Arguments:**
        *comment_id*: Comment ID

    **Returns:**
        ``{'status': '<status>'}``
    '''

    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user:
        return HttpResponse("{'status': 'failed', 'code': 1}")

    comment.comment_text = request.POST['comment_text']
    comment.rating_value = float(request.POST['rating_value'])
    comment.save()

    return HttpResponse("{'status': 'success'}")


@login_required
def comment_vote(request, comment_id, value):
    ''' Upvote or downvote a comment based on value

    **Arguments:**
        *comment_id*: Comment ID
        *value*: The value as +1 or -1

    **Returns:**
        ``{'status': '<status>'}``
    '''

    comment = get_object_or_404(Comment, id=comment_id)
    delta = value
    vote = CommentVote.objects.filter(comment=comment.id, user=request.user.id)
    if len(vote) == 0:
        vote = CommentVote(comment=comment, user=request.user, value=value)
    else:
        vote = vote[0]
        delta = value - vote.value

    vote.value = value
    vote.save()

    comment.votes += delta
    comment.save()

    return HttpResponse("{'status': 'success'}")


@login_required
def dish(request, dish_id):
    ''' Gets all the comments on the dish

    **Arguments:**
        *dish_id*: Dish ID

    **Returns:**
        ``[<comment json object>, <comment json object>, ...]``
    '''

    comments = Comment.objects.filter(dish=dish_id)

    return HttpResponse(json.dumps([json.loads(comment.json()) for comment in comments]))


@login_required
def restaurant(request, restaurant_id):
    ''' Gets all the comments on the dish

    **Arguments:**
        *restaurant_id*: Restaurant ID

    **Returns:**
        ``[<comment json object>, <comment json object>, ...]``
    '''

    comments = Comment.objects.filter(dish=dish_id)

    return HttpResponse(json.dumps([json.loads(comment.json()) for comment in comments]))


@login_required
def user(request):
    ''' Gets all the comments on the dish by the current logged in user

    **Arguments:**
        *user_id*: User ID

    **Returns:**
        ``[<comment json object>, <comment json object>, ...]```
    '''

    comments = Comment.objects.filter(user=request.user.id)

    return HttpResponse(json.dumps([json.loads(comment.json()) for comment in comments]))


@login_required
def dish_new(request, dish_id):
    ''' Creates a new comment on a dish

    **Arguments:**
        *dish_id*: Dish ID

    **Returns:**
        ``{'status': '<status>', 'id': <comment id>}``
    '''
    dish = get_object_or_404(Dish, id=dish_id)

    rating_value = float(request.POST['rating_value'])
    if rating_value < 0 or rating_value > 5:
        return HttpResponse("{'status': 'failed'}")

    comment = Comment(user=request.user, rating_value=rating_value, dish=dish, restaurant=dish.restaurants.all()[0], comment_text=request.POST['comment_text'])
    comment.save()

    return HttpResponse(json.dumps({'status': 'success', 'id': comment.id}))


@login_required
def restaurant_new(request, restaurant_id):
    ''' Creates a new comment on a restaurant

    **Arguments:**
        *restaurant_id*: Restaurant ID

    **Returns:**
        ``{'status': '<status>', 'id': <comment id>}``
    '''
    restaurant = get_object_or_404(Restaurant, id=dish_id)

    rating_value = float(request.POST['rating_value'])
    if rating_value < 0 or rating_value > 5:
        return HttpResponse("{'status': 'failed'}")

    comment = Comment(rating_value=rating_value, dish=None, restaurant=restaurant, comment_text=request.POST['comment_text'])
    comment.save()

    return HttpResponse(json.dumps({'status': 'success', 'id': comment.id}))
