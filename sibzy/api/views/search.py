import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from sibzy.api.models import Restaurant
import json

def search(request, q):
    restaurants = Restaurant.objects.filter(name__icontains=q)
    rs = []
    for restaurant in restaurants:
        rs.append({
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
        })
    return HttpResponse(json.dumps(rs))
    