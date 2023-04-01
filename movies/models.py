from django.db import models


# Create your models here.


class Movies(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=10, null=True, blank=True)
    runtime = models.CharField(max_length=10, null=True)
    cast = models.CharField(max_length=100, null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    director = models.CharField(max_length=100, null=True, blank=True)
    producer = models.CharField(max_length=100, null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    imdb_url = models.CharField(max_length=200)
    thumbnail_url = models.CharField(max_length=200, null=True, blank=True)