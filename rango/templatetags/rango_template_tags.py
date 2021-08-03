from django import template
from rango.models import Category, Area

register = template.Library()

@register.inclusion_tag('rango/areas.html')
def get_area_list(current_area= None):
    return {'areas': Area.objects.all(), 'current_category': current_area}