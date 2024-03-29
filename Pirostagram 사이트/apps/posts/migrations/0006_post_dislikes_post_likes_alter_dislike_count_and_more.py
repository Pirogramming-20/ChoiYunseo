# Generated by Django 5.0.1 on 2024-01-22 13:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.ManyToManyField(related_name='disliked_posts', through='posts.DisLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='liked_posts', through='posts.Like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dislike',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='like',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
