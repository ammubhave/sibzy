from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'load/([A-Za-z0-9_/]+)$', 'sibzy.api.views.load'),
    
    url(r'restaurant/(\w+)$', 'sibzy.api.views.restaurant_profile'),
    
    url(r'search/([A-Za-z0-9 _\\-]+)$', 'sibzy.api.views.search'),
    url(r'test$', 'sibzy.api.views.test_view'),
)