from django.shortcuts import render
from restaurant.models import RestaurantEntry

def profile(request):
    
    
    response = HttpResponse(json.dumps({'status': 'success'}))
    response.set_cookie('fbaccess_token', '')
    response.set_cookie('fbid', '')
    logout(request)
    return response
