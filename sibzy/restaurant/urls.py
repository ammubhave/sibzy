from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^load/profile', 'frontend.views.load_template', {'template_path': 'restaurant_profile'}),
    url(r'^profile/(.*)$', 'restaurant.views.profile'),
    url(r'^initdb', 'restaurant.views.fill_locations'),
    url(r'^scrape', 'restaurant.views.test_view'),
)
