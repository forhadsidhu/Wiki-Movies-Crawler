from rest_framework import serializers
from django.apps import apps
from .models import  WikiApi


class WikiAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = WikiApi
        fields = ('movie_title', 'movie_link', 'movie_year', 'movie_nomination')
