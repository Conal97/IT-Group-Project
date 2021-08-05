from django import template
from rango.models import Area

register = template.Library()

@register.inclusion_tag('rango/areas.html')
def get_area_list(current_area= None):
    return {'areas': Area.objects.all(), 'current_area': current_area}