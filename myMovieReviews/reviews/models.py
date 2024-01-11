from django.db import models

# Create your models here.

class Review(models.Model) :
    GENRE_CHOICES = [
        ('action', 'action'),
        ('comedy', 'comedy'),
        ('drama', 'drama'),
        ('romance', 'romance'),
        ('SF', 'SF')
    ]

    title = models.CharField(max_length=32)
    release_year = models.CharField(max_length=32)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    star_score = models.FloatField()
    running_time = models.IntegerField()
    content = models.TextField()
    director = models.CharField(max_length=32)
    actor = models.CharField(max_length=32)