from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^login/fb$', 'auth.views.login_fb'),
    url(r'^logout$', 'auth.views.logout'),
)
