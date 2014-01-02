from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Backend API urls
    url(r'^!/auth/', include('auth.urls')),
    url(r'^!/', include('backend.urls')),

    # Admin Site urls
    url(r'^admin/', include(admin.site.urls)),

    # All else pass to frontend
    url(r'', include('frontend.urls')),
)
