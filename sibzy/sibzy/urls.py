from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Backend API urls
    url(r'^!/auth/', include('auth.urls')),
    url(r'^auth/', include('auth.urls_noajax')),

    url(r'^!/restaurant/', include('restaurant.urls')),
    url(r'^restaurant/', include('restaurant.urls_noajax')),

    url(r'^!/comment/', include('comment.urls')),

    url(r'^!/search/', include('search.urls')),
    url(r'^search/', include('search.urls_noajax')),

    url(r'^!/frontend/', include('frontend.urls')),

    # Restaurant admin
    url(r'^!/edit/new$', 'restaurant.views.profile_edit_new'),
    url(r'^!/edit/(.*)/edit$', 'restaurant.views.profile_edit'),
    url(r'^!/edit/(.*)/save$', 'restaurant.views.profile_edit_save'),

    # Admin Site urls
    url(r'^admin/', include(admin.site.urls)),

#    url(r'^facebook/', include('django_facebook.urls')),
#    url(r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.


    # All else pass to frontend
    url(r'', include('frontend.urls_noajax')),
    url(r'survey/', TemplateView.as_view(template_name='survey.html')) 
)