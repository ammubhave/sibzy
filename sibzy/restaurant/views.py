from django.shortcuts import render
# from restaurant.models import Restaurant
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from restaurant.models import *
from auth.models import *
import ujson as json
import urllib2
import re
import contextlib
import math
from django.contrib.auth.decorators import login_required


def profile_edit_new(request):
    restaurant_rating = RestaurantRating.objects.create(total=0, vegetarian=0, vegan=0, glutenfree=0, peanutfree=0, lactoseint=0, seafoodint=0)
    location = Location.objects.create(latitude=0, longitude=0, city=City.objects.get(name='Cambridge'), state=State.objects.get(name='Massachusetts'), country=Country.objects.get(name='United States'))
    restaurant = Restaurant.objects.create(location=location, rating=restaurant_rating)

    return HttpResponseRedirect('/!/edit/' + str(restaurant.id) + '/edit')


# For restaurant owners, let them edit profiles
def profile_edit(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)

    dishes_all = restaurant.dishes.all()

    for dish in dishes_all:
        dish.categories_json = json.loads(str(dish.categories_json))
        if str(dish.section_json) == '':
            dish.section_json = []
        else:
            dish.section_json = json.loads(str(dish.section_json))

    Restaurant.dishes_all = property(lambda self: dishes_all)

    return render(request, 'restaurant_profile_edit.html', {'restaurant': restaurant})


@csrf_exempt
def profile_edit_save(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)

    if 'name' in request.REQUEST:
        restaurant.name = request.REQUEST['name']
    if 'description' in request.REQUEST:
        restaurant.description = request.REQUEST['description']
    if 'section_id' in request.REQUEST and 'section_name' in request.REQUEST:
        section = get_object_or_404(DishCategory, id=int(request.REQUEST['section_id']))
        section.name = request.REQUEST['section_name']
        section.save()
    if 'dish_id' in request.REQUEST:
        dish = get_object_or_404(Dish, id=int(request.REQUEST['dish_id']))
        if 'dish_name' in request.REQUEST:
            dish.name = request.REQUEST['dish_name']
        if 'dish_price' in request.REQUEST:
            dish.price = float(request.REQUEST['dish_price'])
        if 'vegetarian' in request.REQUEST:
            if request.REQUEST['vegetarian'] == '1' and len(dish.categories.filter(name='Vegetarian')) == 0:
                dish.categories.add(get_object_or_404(DishCategory, name='Vegetarian'))
            elif request.REQUEST['vegetarian'] == '0' and len(dish.categories.filter(name='Vegetarian')) > 0:
                dish.categories.remove(get_object_or_404(DishCategory, name='Vegetarian'))
            dish.categories_json = json.dumps([x.name for x in dish.categories.all()])
        if 'vegan' in request.REQUEST:
            if request.REQUEST['vegan'] == '1' and len(dish.categories.filter(name='Vegan')) == 0:
                dish.categories.add(get_object_or_404(DishCategory, name='Vegan'))
            elif request.REQUEST['vegan'] == '0' and len(dish.categories.filter(name='Vegan')) > 0:
                dish.categories.remove(get_object_or_404(DishCategory, name='Vegan'))
            dish.categories_json = json.dumps([x.name for x in dish.categories.all()])
        if 'organic' in request.REQUEST:
            if request.REQUEST['organic'] == '1' and len(dish.categories.filter(name='Organic')) == 0:
                dish.categories.add(get_object_or_404(DishCategory, name='Organic'))
            elif request.REQUEST['organic'] == '0' and len(dish.categories.filter(name='Organic')) > 0:
                dish.categories.remove(get_object_or_404(DishCategory, name='Organic'))
            dish.categories_json = json.dumps([x.name for x in dish.categories.all()])
        if 'nutfree' in request.REQUEST:
            if request.REQUEST['nutfree'] == '1' and len(dish.categories.filter(name='Nutfree')) == 0:
                dish.categories.add(get_object_or_404(DishCategory, name='Nutfree'))
            elif request.REQUEST['nutfree'] == '0' and len(dish.categories.filter(name='Nutfree')) > 0:
                dish.categories.remove(get_object_or_404(DishCategory, name='Nutfree'))
            dish.categories_json = json.dumps([x.name for x in dish.categories.all()])
        if 'glutenfree' in request.REQUEST:
            if request.REQUEST['glutenfree'] == '1' and len(dish.categories.filter(name='Glutenfree')) == 0:
                dish.categories.add(get_object_or_404(DishCategory, name='Glutenfree'))
            elif request.REQUEST['glutenfree'] == '0' and len(dish.categories.filter(name='Glutenfree')) > 0:
                dish.categories.remove(get_object_or_404(DishCategory, name='Glutenfree'))
            dish.categories_json = json.dumps([x.name for x in dish.categories.all()])
        dish.save();
    if 'new_section' in request.REQUEST:
        section = DishCategory.objects.create(name=request.REQUEST['new_section'])
        dish = Dish.objects.create(name='New Dish', section=section, price=0, categories_json='[]')
        dish.section_json = json.dumps({'id': section.id, 'name': section.name})
        dish.serialize()
        restaurant.dishes.add(dish)
    if 'new_dish' in request.REQUEST:
        section = DishCategory.objects.get(id=int(request.REQUEST['section']))
        dish = Dish.objects.create(name=request.REQUEST['new_dish'], section=section, price=0, categories_json='[]')
        dish.section_json = json.dumps({'id': section.id, 'name': section.name})
        dish.serialize()
        restaurant.dishes.add(dish)

    restaurant.save()
    return HttpResponse("{'status': 'success'}");

# initialize database
def fill_locations(request):
    country_usa = Country(name='United States')

    if len(Country.objects.filter(name='United States')) == 0:
        country_usa.save()
    else:
        country_usa = Country.objects.get(name='United States')

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
        else:
            state = State.objects.get(name=state_name)
        
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



def printdishes(s):
    dishes = p.findall(s)
def populateFromGrubhub():

    #Grubhub scraper for Cambridge area
    text = urllib2.urlopen("https://www.grubhub.com/search/Cambridge,_MA/").read()

    urls = re.findall('data-restaurant-id="(.*?)"', text)
    p = re.compile('<li class="item.*?<span class="name.*?">([a-zA-Z0-9 \']*?)</span>\s*<span class="price"><span class="dollarSign">\$</span>(.*?)</span>', flags = re.DOTALL)
    urls.pop(1)

    for url in urls:
        listing = []
        with contextlib.closing(urllib2.urlopen("https://www.grubhub.com/restaurant/" + url)) as spage:
            s = spage.read()
            name = re.search('<div itemprop="name">(.*?)</div>', s)
            if len(Restaurant.objects.filter(name=name.group(1))) > 0:
                print 'Exists: ', name.group(1)
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
            cuisines = re.findall('<span itemprop="servesCuisine">(.*?)</span>', s)
            loc = Location(latitude = latitude.group(1), longitude = longitude.group(1), address = street.group(1), city = City.objects.get(name = 'Cambridge'), state = State.objects.get(name = 'Massachusetts'), country = Country.objects.get(name = "United States"), phone = telephone.group(1))
            loc.save()
            dishes = p.findall(s) #dish menu
            sampledishlist = []
            for dish in dishes:       
                categ = DishCategory.objects.filter(name='Main')
                if len(categ) == 0:
                    categ = DishCategory(name = 'Main')
                    categ.save()
                else:
                    categ = categ[0] 

                dish = Dish(name = dish[0], tag = dish[0], price = dish[1].rstrip('+'), section=categ )
                #dish = Dish(name = dish[0], tag = dish[0], price = dish[1].rstrip('+'), vegetarian = len(dish[0])%2, vegan = len(dish[0])%2, gluten = len(dish[0])%2 )
                dish.section_json = json.dumps({'id': categ.id, 'name': categ.name})
                dish.categories_json = '[]'
                dish.save()

                sampledishlist.append(dish)

            rating = RestaurantRating(total = 1, vegetarian = 1, vegan = 1, glutenfree = 1, peanutfree = 1, lactoseint = 1, seafoodint = 1)
            rating.save()
            cool = Restaurant(name = name.group(1), location = loc, rating= rating)
            cool.save()

            for cuisine in cuisines:
                categ = RestaurantCategory.objects.filter(name=cuisine[0])
                if len(categ) == 0:
                    categ = RestaurantCategory(name=cuisine[0])
                    categ.save()
                else:
                    categ = categ[0]
                cool.category.add(categ)

            # print name.group(1)
            for dish in sampledishlist:
                cool.dishes.add(dish)

            cool.json = ''
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
    response = HttpResponse(restaurant.json)
    return response


@login_required
def profile_noajax(request, restaurant_id):
    ''' Return the restaurant profile page corresponsing to restaurant_id

    **Arguments:**
        *restaurant_id*: The numeric ID of the restaurant

    **Returns:**
        ``HTML Response``

    '''

    restaurant = Restaurant.objects.get(id=restaurant_id)
    q = ''
    if 'HTTP_REFERER' in request.META and '/search/q/' in request.META['HTTP_REFERER']:
        q = request.META['HTTP_REFERER'][request.META['HTTP_REFERER'].rfind('/') + 1:]

    RestaurantRating.total_display = property(lambda self: 24*int(math.ceil(self.total)))
    RestaurantRating.total_display_negative = property(lambda self: 24*(5-int(math.ceil(self.total))))
    #print restaurant.rating.total_display
    #restaurant.rating['total_display']

    #for dish in Dish.objects.all():
    #    dish.section_json = json.dumps({'id': dish.section.id, 'name': dish.section.name})
    #    dish.save()

    dishes_all = restaurant.dishes.all()

    profile = UserProfile.objects.get(user=request.user.id)
    for dish in dishes_all:
        if dish.categories_json == None: dish.categories_json = '[]'
        dish.categories_json = json.loads(str(dish.categories_json))
        dish.section_json = json.loads(str(dish.section_json))

        if not ((profile.vegetarian == 0) or (profile.vegetarian == 1 and 'Vegetarian' in dish.categories_json) or (profile.vegetarian == -1 and 'Vegetarian' not in dish.categories_json)):
            dish.name = ''
        if not ((profile.vegan == 0) or (profile.vegan == 1 and 'Vegan' in dish.categories_json) or (profile.vegan == -1 and 'Vegan' not in dish.categories_json)):
            dish.name = ''
        if not ((profile.organic == 0) or (profile.organic == 1 and 'Organic' in dish.categories_json) or (profile.organic == -1 and 'Organic' not in dish.categories_json)):
            dish.name = ''
        if not ((profile.nutfree == 0) or (profile.nutfree == 1 and 'Nutfree' in dish.categories_json) or (profile.nutfree == -1 and 'Nutfree' not in dish.categories_json)):
            dish.name = ''
        if not ((profile.glutenfree == 0) or (profile.glutenfree == 1 and 'Glutenfree' in dish.categories_json) or (profile.glutenfree == -1 and 'Glutenfree' not in dish.categories_json)):
            dish.name = ''

    Restaurant.dishes_all = property(lambda self: dishes_all)
    

    return render(request, 'restaurant_profile_noajax.html', {'restaurant': restaurant, 'q': q})
