from django.urls import path, re_path

from . import views


app_name = 'tree_menu'

# TODO pages...
urlpatterns = [
    re_path(r'', views.first_menu, name='first_menu')
]
