# Generated by Django 3.0.5 on 2020-05-11 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_comment_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='comment',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='comment',
            field=models.ManyToManyField(blank=True, null=True, to='blog.Comment'),
        ),
    ]