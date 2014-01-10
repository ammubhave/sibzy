from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^login/fb$', 'auth.views.login_fb'),
    url(r'^logout$', 'auth.views.logout_fb'),
    url(r'^load/me$', 'auth.views.me'),
    url(r'^load/survey$', 'frontend.views.load_template', {'template_path': 'auth_survey'}),
)