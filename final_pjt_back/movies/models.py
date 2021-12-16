from django.db import models
from django.conf import settings

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}: {self.name}' 


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    # popularity = models.FloatField()
    # vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genre_ids = models.ManyToManyField(Genre)
    recommend_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='recommend_movies')

    def __str__(self):
        return f'{self.pk}: {self.title}' 