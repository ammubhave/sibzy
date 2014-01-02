from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Backend API urls
    url(r'^!/auth/', include('auth.urls')),
    url(r'^!/backend/', include('backend.urls')),
    url(r'^!/restaurants/', include('restaurants.urls')),
    url(r'^!/comments/', include('comments.urls')),
    url(r'^!/search/', include('search.urls')),

    # Admin Site urls
    url(r'^admin/', include(admin.site.urls)),

    # All else pass to frontend
    url(r'', include('frontend.urls')),
)
