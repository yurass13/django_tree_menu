from django.urls import path, re_path

from . import views


app_name = 'tree_menu'

urlpatterns = [
    re_path(r'.+/', views.first_menu),
]
