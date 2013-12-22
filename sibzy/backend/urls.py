from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    # All Static pages
    url(r'^load/home$', 'backend.views.load_template', {'template_path': 'home'}),
    url(r'^load/about$', 'backend.views.load_template', {'template_path': 'about'}),
    url(r'^load/theteam$', 'backend.views.load_template', {'template_path': 'theteam'}),
    url(r'^load/search$', 'backend.views.load_template', {'template_path': 'search'}),
)
