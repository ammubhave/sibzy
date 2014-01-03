from django.contrib import admin
from restaurant.models import Restaurant, Location, RestaurantRating, State, Country


admin.site.register(Restaurant)
admin.site.register(Location)
admin.site.register(RestaurantRating)
admin.site.register(State)
admin.site.register(Country)
