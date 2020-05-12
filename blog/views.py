from django.shortcuts import render, redirect
from . import models, forms


def blog(request):
    posts = models.BlogPost.objects.all().order_by('-date_added')
    return render(request, 'blog/blog.html', {'posts': posts})


def comment(request, id):
    post = models.BlogPost.objects.get(id=id)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            post.comment.add(form.save())
            return redirect('comment', id)
    else:
        form = forms.CommentForm()
    return render(request, 'blog/comment.html', {'post': post, 'form': form})
