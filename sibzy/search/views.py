from django.shortcuts import render
from restaurant.models import Restaurant
from django.http import HttpResponse
import json


def q(request, query):
    restaurants = Restaurant.objects.filter(name__icontains=query)

    response = HttpResponse(json.dumps([json.loads(restaurant.json()) for restaurant in restaurants]))
    return response
