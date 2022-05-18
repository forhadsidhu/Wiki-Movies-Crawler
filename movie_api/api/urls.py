from django.urls import  path
from .views import WikiAPIView,DetailWikiAPIView

urlpatterns = [
    path('',WikiAPIView.as_view()),
    path('<int:pk>/', DetailWikiAPIView.as_view()),
]