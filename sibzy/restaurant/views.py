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

text = urllib2.urlopen("https://www.grubhub.com/search/Cambridge,_MA/").read()

urls = re.findall('data-restaurant-id="(.*?)"', text)
p = re.compile('<li class="item.*?<span class="name.*?">([a-zA-Z0-9 \']*?)</span>\s*<span class="price"><span class="dollarSign">\$</span>(.*?)</span>', flags = re.DOTALL)
urls.pop(1)

def printdishes(s):
    dishes = p.findall(s)
        #for dish in dishes:
        #    dish[0] + "', '" + dish[1]
def populateFromGrubhub():
    for url in urls:
        #print url
        listing = []
        with contextlib.closing(urllib2.urlopen("https://www.grubhub.com/restaurant/" + url)) as spage:
            s = spage.read()
            name = re.search('<div itemprop="name">(.*?)</div>', s)
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
            # if (city.group(1) )
            loc = Location(latitude = latitude.group(1), longitude = longitude.group(1), address = street.group(1), city = City.objects.get(name = 'Boston'), state = State.objects.get(name = 'Massachusetts'), country = Country.objects.get(name = "United States"), phone = telephone.group(1))
            loc.save()
            dishes = p.findall(s) #dish menu
            sampledishlist = []
            for dish in dishes:
                # categ = DishCategory(name = 'a', slug = 'b')
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
            #dishes = p.findall(s)
            #for dish in dishes:
            #    dish[0] + "', '" + dish[1]

            #printdishes(s)
            
def test_view(request):
    #
    #l = Location(lati, l , )
    #rr = RestaurantRating(total=0, ve= -0 , sd= 0)
    #r = Restaurant(name=, location=l, rating=rr, )
    #r.save()
    populateFromGrubhub()
    return HttpResponse("OK")

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

<<<<<<< HEAD
def fill_locations(request):

    country_usa = Country(name='United States')
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
        state.save()
        
        if state.name == 'Massachusetts':
            cambridge = City(name='Cambridge', state=state)
            cambridge.save()
            boston = City(name='Boston', state=state)
            boston.save()
            lexington = City(name='Lexington', state=state)
            lexington.save()

    return HttpResponse("OK")
=======
def methodhere(request):
    pass
>>>>>>> e01db84f1763a7bb8d48cfc598bb08009e063d16
