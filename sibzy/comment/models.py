from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from restaurant.models import *
import json


class Comment(models.Model):
    ''' Comment '''

    #: :py:class:'django.contrib.auth.models.User`: The user who commented
    user = models.ForeignKey(User, null=True)

    #: :py:class:`restaurant.models.Restaurant`: The restaurant on which this comment was given.
    restaurant = models.ForeignKey(Restaurant)

    #: :py:class:`restaurant.models.Dish`: The dish on which this comment was given.
    dish = models.ForeignKey(Dish)

    #: FloatField: The rating from 0 to 5
    rating_value = models.FloatField(default=0)

    #: TextField: The comment text
    comment_text = models.TextField(blank=True)

    #: IntegerField: The votes on this comment
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.dish.name

    def json(self):
        return json.dumps({
            'id': self.id,
            'user': json.loads(self.user.json()),
            'restaurant': self.restaurant.id,
            'dish': self.dish.id,
            'rating_value': self.rating_value,
            'comment_text': self.comment_text,
            'votes': self.votes,
        })

class CommentVote(models.Model):
    ''' Comment Vote'''

    #: :py:class:'django.contrib.auth.models.User`: The user who commented
    user = models.ForeignKey(User)

    #: :py:class:`comment.Comment`: The comment on which this vote is done on
    comment = models.ForeignKey(Comment)

    #: IntegerField: The value of this comment
    value = models.IntegerField(default=0)

    def __str__(self):
        return str(value)

    def json(self):
        return json.dumps({
            'id': self.id,
            'comment': self.comment.id,
            'value': self.value,
        })