from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def num_format(value):
    return str.format("{0:02.2f}", float(str(value))).zfill(5)
