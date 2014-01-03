from django.shortcuts import render
from restaurant.models import Restaurant
from django.http import HttpResponse


def profile(request, restaurant_id):
    ''' Return the restaurant object corresponsing to restaurant_id

    **Arguments:**
        *restaurant_id*: The numeric ID of the restaurant

    **Returns:**
        ``<restaurant JSON object>``

    '''
    
    restaurant = Restaurant.objects.get(id=restaurant_id)

    response = HttpResponse(restaurant.json())
    return response
