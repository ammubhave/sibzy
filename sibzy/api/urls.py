from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'load/([A-Za-z0-9_/]+)$', 'sibzy.api.views.load'),
    url(r'login/fb$', 'sibzy.api.views.auth_fblogin'),
    url(r'logout$', 'sibzy.api.views.auth_logout'),
    
    url(r'restaurant/(\w+)$', 'sibzy.api.views.restaurant_profile'),
    
    url(r'search/([A-Za-z0-9 _\\-]+)$', 'sibzy.api.views.search'),
    url(r'test$', 'sibzy.api.views.test_view'),
    
    url(r'user/profile/get$', 'sibzy.api.views.user_profile_get'),
    url(r'user/profile/put$', 'sibzy.api.views.user_profile_put'),
)