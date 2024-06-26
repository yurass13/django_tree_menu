from django.db import models


class RootItemsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(parent=None)


class Menu(models.Model):
    """
        name:str - unique name of menu. PK.
        title:str - for show in views.
    """
    name = models.SlugField(primary_key=True, max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    # TODO Future $class and $id fields for css manage
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=255, blank=True, default='')
    parent = models.ForeignKey('MenuItem',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               default='',
                               related_name='menu_items',)

    indexes = [
        models.Index(fields=['-parent'])
    ]

    def __str__(self):
        return self.title
