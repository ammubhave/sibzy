from django.contrib import admin
from restaurant.models import Restaurant, RestaurantCategory, Location, RestaurantRating, City, State, Country


admin.site.register(Restaurant)
admin.site.register(RestaurantCategory)
admin.site.register(Location)
admin.site.register(RestaurantRating)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)
