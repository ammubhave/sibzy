from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'frontend.views.load_template', {'template_path': 'home_noajax'}),
    

    # All Static pages
    url(r'^load/home$', 'frontend.views.load_template', {'template_path': 'home_noajax'}),
)