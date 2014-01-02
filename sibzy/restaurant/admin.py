from django.contrib import admin
from restaurant.models import Restaurant, Location, RestaurantRating


admin.site.register(Restaurant)
admin.site.register(Location)
admin.site.register(RestaurantRating)
