from django.db import models
from django.contrib.auth.models import User
import json


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey('Location')
    #category = models.ForeignKey('RestaurantCategory')
    dishes = models.ManyToManyField('Dish', blank=True)  #related_name='restaurants', 
    rating = models.OneToOneField('RestaurantRating', related_name='restaurant')

    def __str__(self):
        return self.name

    def json(self):
        return json.dumps({
            'id': self.id,
            'name': self.name,
            'location': json.loads(self.location.json()),
            'dishes': [json.loads(d.json()) for d in self.dishes.all()],
            'rating': json.loads(self.rating.json()),
        })


class RestaurantCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)


class RestaurantRating(models.Model):
    #restaurant = models.OneToOneField(Restaurant, related_name='rating') - ALREADY EXISTS
    total = models.DecimalField(max_digits=7, decimal_places=1)
    vegetarian = models.DecimalField(max_digits=7, decimal_places=1)
    vegan = models.DecimalField(max_digits=7, decimal_places=1)
    glutenfree = models.DecimalField(max_digits=7, decimal_places=1)
    peanutfree = models.DecimalField(max_digits=7, decimal_places=1)
    lactoseint = models.DecimalField(max_digits=7, decimal_places=1)
    seafoodint = models.DecimalField(max_digits=7, decimal_places=1)
    # TODO: ADD MORE

    def json(self):
        return json.dumps({
            'total': float(self.total),
            'vegetarian': float(self.vegetarian),
            'vegan': float(self.vegan),
            'glutenfree': float(self.glutenfree),
            'peanutfree': float(self.peanutfree),
            'lactoseint': float(self.lactoseint),
            'seafoodint': float(self.seafoodint),
        })


class Location(models.Model):
    latitude = models.DecimalField(max_digits=7, decimal_places=1)
    longitude = models.DecimalField(max_digits=7, decimal_places=1)

    address = models.TextField()
    city = models.CharField(max_length=50)
    #state = models.ForeignKey('State')
   # country = models.ForeignKey('Country')

    phone = models.CharField(max_length=20)

    def __unicode__(self):
        return "{0}, {1}".format(self.address, self.city)

    def json(self):
        return json.dumps({
            'latitude': float(self.latitude),
            'longitude': float(self.longitude),
            'address': self.address,
            'city': self.city,
        })


class State(models.Model):
    name = models.TextField()
    country = models.ForeignKey('Country')

    def __unicode__(self):
        return "{0} - {1}".format(self.name, self.country.name)


class Country(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return "{0}".format(self.name)


class Dish(models.Model):
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places = 2)
    categories = models.ManyToManyField('DishCategory', related_name='dishes')

    @property
    def ratings(self):
        return DishRating.objects.filter(dish=self.id)

    #restaurants = models.ManyToManyFields(Restaurant, related_name='dishes') - ALREADY EXISTS BY DEFAULT

    def json(self):
        return json.dumps({
            'name': self.name,
            'tag': self.tag,
            'price': float(self.price),
            'categories': [json.loads(c.json()) for c in self.categories],
        })


class DishCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    #dishes = models.ManyToManyFields(Dish, related_name='categories') - ALREADY EXISTS BY DEFAULT

    def json(self):
        return json.dumps({
            'name': self.name,
            'slug': self.slug,
        })


class DishRating(models.Model):
    dish = models.ForeignKey(Dish)
    restaurant = models.ForeignKey(Restaurant)
    user = models.ForeignKey(User)
    value = models.IntegerField(default=0)
    comment = models.TextField(blank=True)
    dtadded = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        return super(DishRating, self).save(*args, **kwargs)
