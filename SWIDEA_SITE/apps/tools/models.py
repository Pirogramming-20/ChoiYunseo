from django.db import models

# Create your models here.
class Tool(models.Model):
    title = models.CharField('이름:', max_length=24)
    type = models.CharField('종류:', max_length=24)
    content = models.TextField('개발툴 설명:')

    def __str__(self):
        return self.title