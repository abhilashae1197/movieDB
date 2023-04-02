from django.urls import path
from . import views


urlpatterns = [

    path('movie-list/', views.MovieListCreateAPIView.as_view()),
    path('movie/<int:pk>/', views.MovieCreateReterieveUpdateAPIView.as_view()),
    path('movie/', views.MovieCreateReterieveUpdateAPIView.as_view()),
    path('add-movie/', views.MovieFormView.as_view()),
    path('fetch-movie/', views.movie_imdb_form),
    path('movie-info/', views.movie_info),
]
