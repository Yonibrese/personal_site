# Generated by Django 3.0.5 on 2020-05-11 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200511_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(null=True),
        ),
    ]
