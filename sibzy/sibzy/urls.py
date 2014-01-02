from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Backend API urls
    url(r'^!/auth/', include('auth.urls')),
    url(r'^!/restaurant/', include('restaurant.urls')),
    url(r'^!/comment/', include('comment.urls')),
    url(r'^!/search/', include('search.urls')),
    url(r'^!/frontend/', include('frontend.urls')),

    # Admin Site urls
    url(r'^admin/', include(admin.site.urls)),

    # All else pass to frontend
    url(r'', include('frontend.urls')),
)