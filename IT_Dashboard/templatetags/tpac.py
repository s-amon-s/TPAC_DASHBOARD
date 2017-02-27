from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='lower')
@stringfilter # convery everything coming in as input into string
def lower(value):
    return value.lower()

@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')
