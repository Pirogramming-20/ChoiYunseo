# Generated by Django 5.0.1 on 2024-01-17 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='작성일')),
                ('title', models.CharField(max_length=24, verbose_name='아이디어명:')),
                ('photo', models.ImageField(blank=True, upload_to='images/%Y%m%d', verbose_name='Image:')),
                ('content', models.TextField(verbose_name='아이디어 설명:')),
                ('like', models.IntegerField(default=0, verbose_name='아이디어 관심도:')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.tool', verbose_name='예상 개발툴:')),
            ],
        ),
    ]
