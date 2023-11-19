from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', include('tree_menu.urls', namespace='tree_menu')),
]
