from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'frontend.views.load_template', {'template_path': 'base'}),

    # All Static pages
    url(r'^load/home$', 'frontend.views.load_template', {'template_path': 'home'}),
    url(r'^load/about$', 'frontend.views.load_template', {'template_path': 'about'}),
    url(r'^load/landing$', 'frontend.views.load_template', {'template_path': 'landing'}),
    url(r'^load/theteam$', 'frontend.views.load_template', {'template_path': 'theteam'}),
    url(r'^load/search$', 'frontend.views.load_template', {'template_path': 'search'}),
)