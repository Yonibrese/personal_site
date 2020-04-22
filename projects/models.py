from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    screen_shot = models.ImageField(upload_to='projects/images/%Y/%m/%d',null=True, blank=True)
    url = models.URLField(max_length=200)
    description = models.TextField(null=True)
