from django.urls import path
from . import views


urlpatterns = [

    path('MovieLCapi/', views.MovieListCreateAPI.as_view()),
    path('MovieRUapi/<int:pk>/', views.MovieCreateReterieveUpdateAPI.as_view()),
    path('MovieRUapi/', views.MovieCreateReterieveUpdateAPI.as_view()),
    path('MovieAdd/', views.MovieFormView.as_view()),
]
