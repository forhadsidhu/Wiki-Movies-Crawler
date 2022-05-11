from django.db import models


class Movies(models.Model):
    movie_title = models.CharField(max_length=250)
    movie_link = models.CharField(max_length=250)
    movie_year = models.CharField(max_length=255)
    movie_nomination = models.CharField(max_length=255)

