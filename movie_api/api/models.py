from django.db import models


class WikiApi(models.Model):
    movie_title = models.CharField(max_length=250)
    movie_link = models.CharField(max_length=250)
    movie_year = models.CharField(max_length=100)
    movie_nomination = models.CharField(max_length=13)

    def __str__(self):
        return self.movie_title
