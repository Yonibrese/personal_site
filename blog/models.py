from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=100)
    date_added = models.DateField(auto_now=True)
    comment_text = models.TextField(null=True)

    def __str__(self):
        return f'{self.author, self.date_added}'


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    date_added = models.DateField(auto_now=True)
    blog_text = models.TextField(null=True)
    comment = models.ManyToManyField(Comment)




