from django.contrib import admin
from . import models


@admin.register(models.WoodObjects)
class WoodObjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_added']


