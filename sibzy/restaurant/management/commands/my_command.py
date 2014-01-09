# sibzy/www/sibzy/sibzy/management/commands/my_command.py

from django.core.management.base import NoArgsCommand
from django.template import Template, Context
from django.conf import settings

import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from restaurant.models import *
import json
import urllib2
import re
import contextlib

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        
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
                    loc = Location(latitude = latitude.group(1), longitude = longitude.group(1), address = street.group(1), city = City.objects.get(name = city.group(1)), state = State.objects.get(name = state.group(1)), country = Country.objects.get(name = "United States"), phone = telephone.group(1))
                    loc.save()
                    dishes = p.findall(s) #dish menu
                    sampledishlist = []
                    for dish in dishes:
                        categ = DishCategory(name = 'a', slug = 'b')
                        categ.save()
                        dish = Dish(name = dish[0], tag = dish[0], price = dish[1].rstrip('+'), vegetarian = len(dish[0])%2, vegan = len(dish[0])%2, gluten = len(dish[0])%2 )
                        dish.save()
                        dish.categories.add(categ)
                        dish.save()
                        sampledishlist.append(dish)

                    rating = RestaurantRating(total = 1, vegetarian = 1, vegan = 1, glutenfree = 1, peanutfree = 1, lactoseint = 1, seafoodint = 1)
                    rating.save()
                    cool = Restaurant(name = name.group(1), location = loc, dishes = sampledishlist,rating= rating)
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

        # t=Template("My name is {myname}.")
        # c=Context({"myname":"John"})
        # f = open('write_test.txt', 'w')
        # f.write(t.render(c))
        # f.close