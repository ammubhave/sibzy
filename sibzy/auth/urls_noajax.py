from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^logout$', 'auth.views.logout_user', name='logout_user'),
    url(r'^me$', 'auth.views.me_noajax'),
    url(r'^me/save$', 'auth.views.me_save_noajax'),
)