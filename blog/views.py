from django.shortcuts import render
from . import models


def blog(request):
    posts = models.BlogPost.objects.all().order_by('-date_added')
    return render(request, 'blog/blog.html', {'posts': posts})
