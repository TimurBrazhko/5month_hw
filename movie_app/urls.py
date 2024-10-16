from django.urls import path
from movie_app import views

urlpatterns = [
    path('directors/', views.directors_list_create_api_view),
    path('directors/<int:id>/', views.directors_detail_api_view),
    path('reviews/', views.review_list_create_api_view),
    path('reviews/<int:id>/', views.review_detail_api_view),
    path('movies/', views.movies_list_api_view),
    path('movies/<int:id>/', views.movie_detail_api_view),
    path('movies/reviews/', views.review_movie_api_view),
]
