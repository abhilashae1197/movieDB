from django.db import models


# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=10, null=True, blank=True)
    runtime = models.CharField(max_length=10, null=True)
    cast = models.CharField(max_length=100, null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    director = models.CharField(max_length=100, null=True, blank=True)
    producer = models.CharField(max_length=100, null=True, blank=True)
    imdb_rating = models.CharField(max_length=10,  null=True, blank=True)
    imdb_url = models.CharField(max_length=200, unique=True)
    thumbnail_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name