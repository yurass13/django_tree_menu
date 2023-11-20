from django import template
from django.shortcuts import get_object_or_404

from ..models import Menu, MenuItem


register = template.Library()


# TODO (Future) check mptt
# https://github.com/django-mptt/django-mptt
@register.inclusion_tag('tree_menu/menu/menu.html')
def draw_menu(menu_name: str): 
    if menu_name is None:
        raise AttributeError("Undefined menu object!")

    menu_obj = get_object_or_404(Menu.objects.select_related(), name=menu_name)

    return {'menu': menu_obj}


@register.filter
def lookup_grouper(grouper, key):
    for group in grouper:
        if group[0] == key:
            return group[1]
    return None