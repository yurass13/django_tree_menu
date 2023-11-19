from typing import Optional
from django import template
from django.shortcuts import get_object_or_404

from ..models import Menu, MenuItem

register = template.Library()


# TODO not optimal ORM query.
# NOTE need build recursive query or use mptt extension or ect.
# https://github.com/django-mptt/django-mptt
@register.inclusion_tag('tree_menu/menu_template.html')
def draw_menu(menu_name: Optional[str] = None, 
         parent_id: Optional[int] = None,
         level:int = 0):
    if menu_name is None and parent_id is None:
        raise AttributeError("Undefined menu object!")

    data = {}

    if parent_id is None:
        menu_obj = get_object_or_404(Menu, name=menu_name)
    else:
        menu_obj = get_object_or_404(MenuItem, id=parent_id)

    return {'menu_name': menu_name,
            'level': level,
            'menu_items': menu_obj.menu_items.filter(parent=parent_id) }
