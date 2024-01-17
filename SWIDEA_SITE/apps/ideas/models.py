from django.db import models
from apps.tools.models import Tool

# Create your models here.

class Idea(models.Model):
    title = models.CharField('아이디어명:', max_length=24)
    photo = models.ImageField('Image:', blank=True, upload_to='images/%Y%m%d')
    content = models.TextField('아이디어 설명:')
    like = models.IntegerField('아이디어 관심도:', default=0)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, verbose_name='예상 개발툴:')
    