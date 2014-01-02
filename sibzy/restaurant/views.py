from django.shortcuts import render
from restaurant.models import Restaurant
from django.http import HttpResponse


def profile(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)

    response = HttpResponse(restaurant.json())
    return response
