from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^load/q$', 'frontend.views.load_template', {'template_path': 'search_q'}),

    url(r'^q/(.*)$', 'search.views.q'),
)
