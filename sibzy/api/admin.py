from django.contrib import admin
from sibzy.api.models import *
from django import forms
from django.forms.extras.widgets import *
admin.site.register(Restaurant)
admin.site.register(RestaurantRating)
admin.site.register(Location)
admin.site.register(Dish)


#class ModelListField(ListField):
#    def formfield(self, **kwargs):
#        return FormListField(**kwargs)
#class ListFieldWidget(forms.SelectMultiple):
#    pass
#class ListFormField(forms.Field):
#    """ A form field for being able to display a djangotoolbox.fields.ListField. """
#
#    widget = forms.ListWidget
#
#    def clean(self, value):
#        return [v.strip() for v in value.split(',') if len(v.strip()) > 0]