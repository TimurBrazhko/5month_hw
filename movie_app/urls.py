from django.urls import path
from movie_app import views

urlpatterns = [
    path('directors/', views.DirectorListView.as_view(), name='director_list_api_view'),
    path('directors/<int:id>/', views.DirectorDetailView.as_view(), name='director_detail_api_view'),
    path('reviews/', views.ReviewListView.as_view(), name='review_list_api_view'),
    path('reviews/<int:id>/', views.ReviewDetailView.as_view(), name='review_detail_api_view'),
    path('movies/', views.MovieListView.as_view(), name='movie_list_api_view'),
    path('movies/<int:id>/', views.MovieDetailView.as_view(), name='movie_detail_api_view'),
    # path('movies/reviews/', views.review_movie_api_view),
]
