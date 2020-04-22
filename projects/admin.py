from django.contrib import admin
from . import models


@admin.register(models.Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
