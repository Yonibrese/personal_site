from django.db import models


class WoodObjects(models.Model):
    image = models.ImageField(upload_to='wood_obj/%y/%m/%d', null=True, blank=True)
    type = models.CharField(max_length=100)
    date_added = models.DateField(auto_now=True)
    description = models.TextField(null=True)
