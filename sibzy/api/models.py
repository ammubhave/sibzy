from django.db import models
from django.contrib.auth.models import User
from djangotoolbox.fields import ListField, EmbeddedModelField

class AppSetting(models.Model):
    key = models.CharField(max_length=255)
    value = models.TextField(blank=True)
    
    def __unicode__(self):
        return "{0}: {1}".format(self.key, self.value)

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey('Location')
    #category = models.ForeignKey('RestaurantCategory')
    dishes = ListField(EmbeddedModelField('Dish'), blank=True)#related_name='restaurants', 
    rating = models.OneToOneField('RestaurantRating', related_name='restaurant')
    
    def __str__(self):
        return self.name
    
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
    

class Location(models.Model):
    latitude = models.DecimalField(max_digits=7, decimal_places=1)
    longitude = models.DecimalField(max_digits=7, decimal_places=1)    
   
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    phone = models.CharField(max_length=20)
    
    def __unicode__(self):
        return "{0}, {1}, {2}, {3}".format(self.address, self.city, self.state, self.country)
    
    
class Dish(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField('DishCategory', related_name='dishes')
    
    @property
    def ratings(self):
        return DishRating.objects.filter(dish=self.id)
    
    #restaurants = models.ManyToManyFields(Restaurant, related_name='dishes') - ALREADY EXISTS BY DEFAULT
    
class DishCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    
    #dishes = models.ManyToManyFields(Dish, related_name='categories') - ALREADY EXISTS BY DEFAULT
    
class DishRating(models.Model):
    dish = models.ForeignKey(Dish)
    restaurant = models.ForeignKey(Restaurant)
    user = models.ForeignKey(User)
    value = models.IntegerField(default=0)
    comment = models.TextField(blank=True)
    dtadded = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):        
        return super(DishRating, self).save(*args, **kwargs)
