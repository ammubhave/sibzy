from django.db import models
from django.contrib.auth.models import User
import json


class Restaurant(models.Model):
    ''' Restaurant details '''

    #: CharField(255): Restaurant name
    name = models.CharField(max_length=255)

    #: :py:class:`restaurant.models.Location`: Restaurant location
    location = models.ForeignKey('Location')

    #: ManyToManyField: List of all :py:class:`restaurant.models.RestaurantCategory` this restaurant belongs to
    category = models.ManyToManyField('RestaurantCategory', related_name='restaurants', blank=True)

    #: ManyToManyField: List of all :py:class:`restaurant.models.Dish` this restaurant serves
    dishes = models.ManyToManyField('Dish', related_name='restaurants', blank=True)

    #: OneToOneField: The associated :py:class:`restaurant.models.RestaurantRating`
    rating = models.OneToOneField('RestaurantRating', related_name='restaurant')

    def __str__(self):
        return self.name

    def json(self):
        return json.dumps({
            'id': self.id,
            'name': self.name,
            'location': json.loads(self.location.json()),
            'category': [json.loads(c.json()) for c in self.category.all()],
            'dishes': [json.loads(d.json()) for d in self.dishes.all()],
            'rating': json.loads(self.rating.json()),
        })


class RestaurantCategory(models.Model):
    ''' Restaurant Category '''

    #: CharField(255): Category name
    name = models.CharField(max_length=255)

    #: CharField(255): Unique slug for this category
    slug = models.CharField(max_length=255, unique=True)

    def json(self):
        return json.dumps({
            'name': self.name,
            'slug': self.slug,
        })


class RestaurantRating(models.Model):
    ''' Restaurant Rating (One to one with :py:class:`restaurant.models.Restaurant`) '''

    #restaurant = models.OneToOneField(Restaurant, related_name='rating') - ALREADY EXISTS

    #: DecimalField(6.1): The total restaurant rating
    total = models.DecimalField(max_digits=7, decimal_places=1)

    #: DecimalField(6.1): Vegetarian specific restaurant rating
    vegetarian = models.DecimalField(max_digits=7, decimal_places=1)

    #: DecimalField(6.1): Vegan specific restaurant rating
    vegan = models.DecimalField(max_digits=7, decimal_places=1)

    #: DecimalField(6.1): Gluten free food specific restaurant rating
    glutenfree = models.DecimalField(max_digits=7, decimal_places=1)

    #: DecimalField(6.1): Peanut free food specific restaurant rating
    peanutfree = models.DecimalField(max_digits=7, decimal_places=1)

    #: DecimalField(6.1): Lactose free food specific restaurant rating
    lactoseint = models.DecimalField(max_digits=7, decimal_places=1)

    #: DecimalField(6.1): Seafood free food specific restaurant rating
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
    ''' Restaurant Location '''

    #: DecimalField(6.1): Location latitude
    latitude = models.DecimalField(max_digits=7, decimal_places=1)

    #: DecimalField(6.1): Location longitude
    longitude = models.DecimalField(max_digits=7, decimal_places=1)

    #: TextField: Location street address, does not include city, state or country
    address = models.TextField()

    #: :py:class:`restaurant.models.City`: Location city
    city = models.ForeignKey('City')

    #: :py:class:`restaurant.models.State`: Location state
    state = models.ForeignKey('State')

    #: :py:class:`restaurant.models.Country`: Location country
    country = models.ForeignKey('Country')

    #: CharField(20): Contact phone number
    phone = models.CharField(max_length=20)

    def __unicode__(self):
        return "{0}, {1}".format(self.address, self.city)

    def json(self):
        return json.dumps({
            'latitude': float(self.latitude),
            'longitude': float(self.longitude),
            'address': self.address,
            'city': self.city.name,
            'state': self.state.name,
            'country': self.country.name,
            'phone': self.phone,
        })


class City(models.Model):
    ''' City '''

    #: TextField: City name
    name = models.TextField()

    #: :py:class:`restaurant.models.State`: State
    state = models.ForeignKey('State')

    def __unicode__(self):
        return "{0}, {1}, {2}".format(self.name, self.state.name, self.state.country.name)

    def json(self):
        return json.dumps({
            'name': self.name,
        })


class State(models.Model):
    ''' State '''

    #: TextField: State name
    name = models.TextField()

    #: :py:class:`restaurant.models.Country`: Country
    country = models.ForeignKey('Country')

    def __unicode__(self):
        return "{0}, {1}".format(self.name, self.country.name)

    def json(self):
        return json.dumps({
            'name': self.name,
        })


class Country(models.Model):
    ''' Country '''

    #: TextField: Country name
    name = models.TextField()

    def __unicode__(self):
        return "{0}".format(self.name)
    
    def json(self):
        return json.dumps({
            'name': self.name,
        })


class Dish(models.Model):
    ''' Dish '''

    #: CharField(255): Dish name
    name = models.CharField(max_length=255)

    #: CharField(255): The tag under which the dish should be categorized
    tag = models.CharField(max_length=255)

    #: DecimalField(5.2): The price in dollars
    price = models.DecimalField(max_digits=7, decimal_places = 2)

    #: ManyToManyField: List of all :py:class:`restaurant.models.DishCategory`
    categories = models.ManyToManyField('DishCategory', related_name='dishes')

    #: Return rating of this dish
    @property
    def ratings(self):
        return DishRating.objects.filter(dish=self.id)

    #restaurants = models.ManyToManyFields(Restaurant, related_name='dishes') - ALREADY EXISTS BY DEFAULT

    def json(self):
        return json.dumps({
            'name': self.name,
            'tag': self.tag,
            'price': float(self.price),
            'categories': [c.name for c in self.categories.all()],
        })
    
    def __str__(self):
        return self.name


class DishCategory(models.Model):
    ''' Dish category '''

    #: CharField(255): Dish name
    name = models.CharField(max_length=255)

    #: CharField(255): Unique slug for this category
    slug = models.CharField(max_length=255, unique=True)

    #dishes = models.ManyToManyFields(Dish, related_name='categories') - ALREADY EXISTS BY DEFAULT

    def json(self):
        return json.dumps({
            'name': self.name,
            'slug': self.slug,
        })
    
    def __str__(self):
        return self.name
    


class DishRating(models.Model):
    ''' Rating given by a single user to a dish '''

    #: :py:class:`restaurant.models.Dish`: The associated dish
    dish = models.ForeignKey(Dish)

    #: :py:class:`restaurant.models.Restaurant`: The assocated restaurant
    restaurant = models.ForeignKey(Restaurant)

    #: :py:class:`django.contrib.auth.models.User`: The user who rated this dish
    user = models.ForeignKey(User)

    #: IntegerField: The rating given
    value = models.IntegerField(default=0)

    #: TextField: Any optional comment by the user
    comment = models.TextField(blank=True)

    #: DateTimeField: The DateTime when this dish was rated
    dtadded = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        return super(DishRating, self).save(*args, **kwargs)
