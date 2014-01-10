from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^dish/(\d+)/new$', 'comment.views.dish_new'),
    url(r'^dish/(\d+)$', 'comment.views.dish'),
    url(r'^restaurant/(\d+)/new$', 'comment.views.restaurant_new'),
    url(r'^restaurant/(\d+)$', 'comment.views.restaurant'),

    url(r'^(\d+)/get$', 'comment.views.comment_get'),
    url(r'^(\d+)/set$', 'comment.views.comment_set'),
    #url(r'^(\d+)/up$', 'comment.views.comment')
)
