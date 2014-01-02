from django.db import models
from django.contrib.auth.models import User

import json


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fbid = models.TextField()
    fbusername = models.TextField(blank=True)
    fbaccess_token = models.TextField(blank=True)
    #dish_category_strong_user = ListField(EmbeddedModelField('DishCategory'), blank=True)
    #dish_category_weak_user = ListField(EmbeddedModelField('DishCategory'), blank=True)
    #dish_category_weak_sys = ListField(EmbeddedModelField('DishCategory'), blank=True)
