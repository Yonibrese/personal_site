from django.shortcuts import render
from . import models


def wood_gallery(request):
    works = models.WoodObjects.objects.all().order_by('-date_added')
    return render(request, 'woodwork/gallery.html', {'works': works})
