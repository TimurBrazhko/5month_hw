from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from movie_app.models import Director, Movie, Review


@api_view(['GET'])
def directors_list_api_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def directors_detail_api_view(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={"detail": "Director not found"}
        )
    data = DirectorSerializer(directors).data
    return Response(data=data)


@api_view(['GET'])
def movies_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={"detail": "Director not found"}
        )
    data = MovieSerializer(movie).data
    return Response(data=data)

@api_view(['GET'])
def review_list_api_view(request):
    review = Review.objects.all()
    data = ReviewSerializer(review,many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={"detail": "Review not found"}
        )
    data = ReviewSerializer(review).data
    return Response(data=data)
