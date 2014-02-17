from django.shortcuts import render
from restaurant.models import Restaurant
from django.http import HttpResponse
import simplejson as json
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def q(request, query):
    ''' Do a search from the query. Search details yet to be implemented.

    **Arguments:**
        *query*: The textual search query from the user

    **Returns:**
        ``[<restaurant object>, <restaurant object>, ...]``
    '''
    #for restaurant in Restaurant.objects.all():
    #    restaurant.serialize()

    restaurants = Restaurant.objects.filter(name__icontains=query)[:10]
    resp = '['
    for restaurant in restaurants:
        # element = {
        #     'id': restaurant.id,
        #     'name': restaurant.name,
        #     'location': json.loads(restaurant.location.json()),
        #     'category': [json.loads(c.json()) for c in restaurant.category.all()],
        #     'rating': json.loads(restaurant.rating.json()),
        # }
        resp += restaurant.json + ','
    if resp == '[':
        resp = '[,'
    #print resp
    resp = resp[:-1] + ']'
    response = HttpResponse(resp)
    return response

@ensure_csrf_cookie
def q_noajax(request, query):
    ''' Do a search from the query. Search details yet to be implemented. Returns search html page.

    **Arguments:**
        *query*: The textual search query from the user

    **Returns:**
        ``HTML Response``
    '''
    #for restaurant in Restaurant.objects.all():
    #    restaurant.serialize()

    restaurants = Restaurant.objects.filter(name__icontains=query)[:10]
    resp = '['
    for restaurant in restaurants:
        # element = {
        #     'id': restaurant.id,
        #     'name': restaurant.name,
        #     'location': json.loads(restaurant.location.json()),
        #     'category': [json.loads(c.json()) for c in restaurant.category.all()],
        #     'rating': json.loads(restaurant.rating.json()),
        # }
        resp += restaurant.json + ','
    if resp == '[':
        resp = '[,'
    #print resp
    resp = resp[:-1] + ']'

    return render(request, 'search_q_noajax.html', {'q': query,
                                                    'restaurants': restaurants,
                                                    'json': resp})

@ensure_csrf_cookie
def set_location(request):
    response = HttpResponse("{'status': 'success'}");
    response.set_cookie('lat', request.REQUEST['lat']);
    response.set_cookie('lng', request.REQUEST['lng']);
    return response
