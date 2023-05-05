from django import template
from salon.models import Salon
register = template.Library()

@register.filter
def is_open(request):
    return "checked" if Salon.objects.filter(is_open=True, user=request.user) else ""

@register.filter(name='short_time')
def short_time(time):
    return time.split(",", 1)[0]