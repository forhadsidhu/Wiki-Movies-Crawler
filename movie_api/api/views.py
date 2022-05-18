from django.shortcuts import render
from django.apps import apps
from .serializers import WikiAPISerializer
from .models import  WikiApi
from rest_framework import generics, permissions


# This way another model of app should import
# book_model = apps.get_model('wikiapi', 'WikiApi')


class WikiAPIView(generics.ListAPIView):
    model = WikiApi
    queryset = model.objects.all()
    serializer_class = WikiAPISerializer


class DetailWikiAPIView(generics.RetrieveUpdateDestroyAPIView):
    model = WikiApi
    queryset = model.objects.all()
    serializer_class = WikiAPISerializer
