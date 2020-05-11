from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    date_added = models.DateField(auto_now=True)
    blog_text = models.TextField(null=True)

