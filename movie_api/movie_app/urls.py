from . views import movie_detail,movies_list
from django.urls import path
urlpatterns = [
  path('movie/<int:pk>/', movie_detail),
  path('movies/count=<int:cnt>/page_size=<int:ps>/page_no=<int:pn>/', movies_list),
]