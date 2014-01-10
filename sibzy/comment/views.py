import os, urllib
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from auth.models import User, UserProfile
from comment.models import Comment
import json


def comment_get(request, comment_id):
    ''' Get the comment with id = comment_id

    **Arguments:**
        *comment_id*: Comment ID

    **Returns:**
        ``<comment json object>``
    '''

    comment = get_object_or_404(Comment, id=comment_id)

    return HttpResponse(comment.json())


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


def dish(request, dish_id):
    ''' Gets all the comments on the dish

    **Arguments:**
        *dish_id*: Dish ID

    **Returns:**
        ``[<comment json object>, <comment json object>, ...]``
    '''

    comments = Comment.objects.filter(dish=dish_id)

    return HttpResponse(json.dumps([json.loads(comment.json()) for comment in comments]))


def restaurant(request, restaurant_id):
    ''' Gets all the comments on the dish

    **Arguments:**
        *restaurant_id*: Restaurant ID

    **Returns:**
        ``[<comment json object>, <comment json object>, ...]``
    '''

    comments = Comment.objects.filter(dish=dish_id)

    return HttpResponse(json.dumps([json.loads(comment.json()) for comment in comments]))


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

    comment = Comment(rating_value=rating_value, dish=dish, restaurant=dish.restaurants_set.all()[0], comment_text=request.POST['comment_text'])
    comment.save()

    return HttpResponse(json.dumps({'status': 'success', 'id': comment.id}))


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
