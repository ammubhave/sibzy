import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from sibzy.api.models import *
import json

def test_view(request):
    #
    #l = Location(lati, l , )
    #rr = RestaurantRating(total=0, ve= -0 , sd= 0)
    #r = Restaurant(name=, location=l, rating=rr, )
    #r.save()
    
    return HttpResponse("OK")
    