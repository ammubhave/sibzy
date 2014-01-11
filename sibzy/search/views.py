from django.shortcuts import render
from restaurant.models import Restaurant
from django.http import HttpResponse
import json


def q(request, query):
    ''' Do a search from the query. Search details yet to be implemented.

    **Arguments:**
        *query*: The textual search query from the user

    **Returns:**
        ``[<restaurant object>, <restaurant object>, ...]``
    '''

    restaurants = Restaurant.objects.filter(name__icontains=query)[:10]
    resp = []
    for restaurant in restaurants:
        element = json.loads(restaurant.json())
        element['dishes'] = None
        resp.append(element)
    response = HttpResponse(json.dumps(resp))
    return response
