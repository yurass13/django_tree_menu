from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Menu, MenuItem


class CompositeMenuMixin:
    def view_total_items(self, obj):
        count = obj.menu_items.count()
        if count == 0:
            return "-"

        url = (
                reverse("admin:tree_menu_menuitem_changelist")
                + "?"
                + urlencode(self.get_query_params(obj))
        )
        return format_html('<a href="{}">{} Items</a>', url, count)

    view_total_items.short_description = "Items"


class MenuItemInline(admin.TabularInline, CompositeMenuMixin):
    model = MenuItem
    fields = ('title', 'url', 'view_total_items')
    readonly_fields = ('view_total_items', )
    ordering = ('-parent', )

    @staticmethod
    def get_query_params(obj):
        return {"menu__name": f"{obj.menu.name}",
                "parent__id": f"{obj.id}"}


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin, CompositeMenuMixin):
    list_display = ['name',
                    'description',
                    'view_total_items',]
    inlines = (MenuItemInline, )

    @staticmethod
    def get_query_params(obj):
        return {"menu__name": f"{obj.name}"}


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin, CompositeMenuMixin):
    """ TODO (Future)
            On create or change:
                1. On chosen menu we should filter dropdown values of parent
                    .filter(menu__name=$chosen_menu_name).
                2. On choosing parent - auto get relation with menu from parent.
                Django built-in static example:
                    https://books.agiliq.com/projects/django-admin-cookbook/en/latest/filter_fk_dropdown.html
                NOTE need js script and endpoint for dynamic update select values.
                    - Inject js script into admin template?
                    - Override filter_fk_dropdown with using subrequest from frontend to get current <select> values?
    """
    list_display = ['title', 'url', 'view_total_items', 'view_menu']

    @staticmethod
    def get_query_params(obj):
        return {"menu__name": f"{obj.menu.name}",
                "parent__id": f"{obj.id}"}

    @staticmethod
    def view_menu(obj):
        name = obj.menu.name
        url = reverse("admin:tree_menu_menu_change", args=(name, ))
        return format_html('<a href="{}">{}</a>', url, name)

    view_menu.short_description = "Menu"
