from django import template
from salon.models import Salon
register = template.Library()

@register.filter
def is_open(request):
    return "checked" if Salon.objects.filter(is_open=True, user=request.user) else ""