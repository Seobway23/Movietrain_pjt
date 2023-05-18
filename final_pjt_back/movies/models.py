from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.TextField()
    release_data = models.DateField()
    created_at = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.FloatField()

class Genre(models.Model):
    genre_id = models.IntegerField()
    genre = models.CharField(max_length=100)

class MovieGenres(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)


class CustomRecommend(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
