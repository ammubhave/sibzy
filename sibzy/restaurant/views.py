from django.shortcuts import render
# from restaurant.models import Restaurant
from django.http import HttpResponse

import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from restaurant.models import *
import json
import urllib2
import re
import contextlib

# For restaurant owners, let them edit profiles
def profile_edit(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    return render(request, 'restaurant_profile_edit.html', {'restaurant': restaurant})

# initialize database
def fill_locations(request):
    country_usa = Country(name='United States')

    if len(Country.objects.filter(name='United States')) == 0:
        country_usa.save()

    states = [
        ('AK', 'Alaska'),
        ('AL', 'Alabama'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('DC', 'Washington D.C.'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming')
    ]

    for (state_code, state_name) in states:

        state = State(name=state_name, country=country_usa)
        if len(State.objects.filter(name=state_name)) == 0:        
            state.save()
        
        if state.name == 'Massachusetts':
            if len(City.objects.filter(name='Cambridge')) == 0:
                cambridge = City(name='Cambridge', state=state)
                cambridge.save()
            if len(City.objects.filter(name='Boston')) == 0:
                boston = City(name='Boston', state=state)
                boston.save()
            if len(City.objects.filter(name='Lexington')) == 0:
                lexington = City(name='Lexington', state=state)
                lexington.save()

    return HttpResponse("Locations have been added to database")


#Grubhub scraper for Cambridge area
text = urllib2.urlopen("https://www.grubhub.com/search/Cambridge,_MA/").read()

urls = re.findall('data-restaurant-id="(.*?)"', text)
p = re.compile('<li class="item.*?<span class="name.*?">([a-zA-Z0-9 \']*?)</span>\s*<span class="price"><span class="dollarSign">\$</span>(.*?)</span>', flags = re.DOTALL)
urls.pop(1)

def printdishes(s):
    dishes = p.findall(s)
def populateFromGrubhub():

    for url in urls:
        listing = []
        with contextlib.closing(urllib2.urlopen("https://www.grubhub.com/restaurant/" + url)) as spage:
            s = spage.read()
            name = re.search('<div itemprop="name">(.*?)</div>', s)
            if len(Restaurant.objects.filter(name= name.group(1))):
                continue
            #address = re.search('<p class="restaurantAddress fine_print">(.*?)</p>', s)
            #print "Address:", address.group(1)
            street = re.search('<span itemprop="streetAddress">(.*?)</span>', s)
            city = re.search('<span itemprop="addressLocality">(.*?)</span>', s)
            state = re.search('<span itemprop="addressRegion">(.*?)</span>', s)
            zipcode = re.search('<span itemprop="postalCode">(.*?)</span>', s)
            pickup = 'data-mp-with-pickup-available="true"' in s
            telephone = re.search('<div itemprop="telephone">(.*?)</div>', s)
            latitude = re.search('<meta itemprop="latitude" content="(.*?)"', s)
            longitude = re.search('<meta itemprop="longitude" content="(.*?)"', s)
            cuisine = re.findall('<span itemprop="servesCuisine">(.*?)</span>', s)
            loc = Location(latitude = latitude.group(1), longitude = longitude.group(1), address = street.group(1), city = City.objects.get(name = 'Boston'), state = State.objects.get(name = 'Massachusetts'), country = Country.objects.get(name = "United States"), phone = telephone.group(1))
            loc.save()
            dishes = p.findall(s) #dish menu
            sampledishlist = []
            for dish in dishes:
                categ = DishCategory.objects.filter(slug = 'b')
                if len(categ) == 0:
                    categ = DishCategory(name = 'a', slug = 'b')
                    categ.save()
                else:
                    categ = categ[0]
                dish = Dish(name = dish[0], tag = dish[0], price = dish[1].rstrip('+') )
                #dish = Dish(name = dish[0], tag = dish[0], price = dish[1].rstrip('+'), vegetarian = len(dish[0])%2, vegan = len(dish[0])%2, gluten = len(dish[0])%2 )
                dish.save()
                dish.categories.add(categ)
                dish.save()
                sampledishlist.append(dish)

            rating = RestaurantRating(total = 1, vegetarian = 1, vegan = 1, glutenfree = 1, peanutfree = 1, lactoseint = 1, seafoodint = 1)
            rating.save()
            cool = Restaurant(name = name.group(1), location = loc, rating= rating)
            cool.save()
            # print name.group(1)
            for dish in sampledishlist:
                cool.dishes.add(dish)
            cool.save()
    return HttpResponse("Cambridge scraping finished")
def test_view(request):
    
    return HttpResponse(populateFromGrubhub())


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
