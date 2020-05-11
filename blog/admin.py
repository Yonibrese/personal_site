from django.contrib import admin
from . import models


@admin.register(models.BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_added']
