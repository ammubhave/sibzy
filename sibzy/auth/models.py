from django.db import models
from django.contrib.auth.models import User

import simplejson as json

User.profile = lambda self: UserProfile.objects.get(user=self.id)

User.json = lambda self: json.dumps({
    'id': self.id,
    'fbid': self.username,
    'fbusername': self.profile().fbusername,
    })


class UserProfile(models.Model):
    ''' Stores the profile details of a user '''

    #: OneToOneField: The :py:class:`django.contrib.auth.models.User` this references to
    user = models.OneToOneField(User)

    #: TextField: The unique Facebook ID of the user
    fbid = models.TextField()

    #: TextField: The Facebook username (if exists) of the user
    fbusername = models.TextField(blank=True)

    #: TextField: The short-lived access token of the user so we can make queries from the server
    #: since we cannot trust the client for the user details
    fbaccess_token = models.TextField(blank=True)

    vegetarian = models.IntegerField(default=0)
    vegan = models.IntegerField(default=0)
    organic = models.IntegerField(default=0)

    # For later
    #dish_category_strong_user = ListField(EmbeddedModelField('DishCategory'), blank=True)
    #dish_category_weak_user = ListField(EmbeddedModelField('DishCategory'), blank=True)
    #dish_category_weak_sys = ListField(EmbeddedModelField('DishCategory'), blank=True)

    def __unicode__(self):
        return self.user.username
