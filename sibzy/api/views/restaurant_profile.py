import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from sibzy.api.models import Restaurant
import json

def restaurant_profile(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    dishes = []
    for dish in restaurant.dishes:
        dishes.append({
            'name': dish.name
        })
    return HttpResponse(json.dumps({
            'name': restaurant.name,
            'location': {
                'latitude': float(restaurant.location.latitude),
                'longitude': float(restaurant.location.longitude),
                'address': restaurant.location.address,
                'city': restaurant.location.city,
                'state': restaurant.location.state,
                'country': restaurant.location.country,
                'phone': restaurant.location.phone,
            },
            'dishes': dishes,
        }))
    