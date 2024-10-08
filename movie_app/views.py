from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer
from movie_app.models import Director, Movie, Review


@api_view(['GET', 'POST'])
def directors_list_create_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.prefetch_related('movies').all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        director = Director.objects.create(
            **request.data
        )
        return Response(data={'director_id': director.id},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def directors_detail_api_view(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={"detail": "Director not found"}
        )

    if request.method == 'GET':
        data = DirectorSerializer(directors).data
        return Response(data=data)

    elif request.method == 'PUT':
        directors.name = request.data.get('name')
        directors.save()
        return Response(data=DirectorSerializer(directors).data,
                        status=status.HTTP_201_CREATED)

    else:
        directors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movies_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        movie = Movie.objects.create(
            **request.data
        )
        return Response(data={'movie_id': movie.id},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={"detail": "Director not found"}
        )

    if request.method == 'GET':
        data = MovieSerializer(movie).data
        return Response(data=data)

    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)

    else:
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_create_api_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewSerializer(review,many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        review = Review.objects.create(
            **request.data
        )
        return Response(data={'review_id': review.id},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={"detail": "Review not found"}
        )
    if request.method == 'GET':
        data = ReviewSerializer(review).data
        return Response(data=data)

    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data,
                        status=status.HTTP_201_CREATED)

    else:
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def review_movie_api_view(request):
    movies = Movie.objects.select_related('director').prefetch_related('reviews').all()
    data = MovieReviewSerializer(movies, many=True).data
    return Response(data=data)
