from django.shortcuts import render
from . import models


def web_projects(request):
    projects = models.Project.objects.all()
    return render(request, 'projects/web_projects.html', {'projects': projects})
