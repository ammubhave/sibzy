from django.shortcuts import render
from restaurant.models import Restaurant


def profile(request):
    restaurant = Restaurant.objects.get(request.GET['id'])

    response = HttpResponse(restaurant.json())
    return response
