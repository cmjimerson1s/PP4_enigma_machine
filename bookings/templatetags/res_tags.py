from django import template
from atexit import register
import imp

register = template.Library()

@register.filter
def res_date(value, arg):
    return value.filter(date=arg)

@register.filter
def res_time(value, arg):
    return value.filter(time_slot=arg)

@register.filter
def res_room(value, arg):
    return value.filter(room_choice=arg)
