from django.db import models
from apps.users.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to='posts/%Y%m%d')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Like(models.Model):
    count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class DisLike(models.Model):
    count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    