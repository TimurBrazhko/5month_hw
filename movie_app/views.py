from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.serializers import (DirectorSerializer,
                                   MovieSerializer,
                                   ReviewSerializer,
                                   MovieReviewSerializer,
                                   DirectorValidationSerializer,
                                   MovieValidationSerializer,
                                   ReviewValidationSerializer,)
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateAPIView)
from movie_app.models import Director, Movie, Review


class DirectorListView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def create(self, request, *args, **kwargs):
        serializer = DirectorValidationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        director = Director.objects.create(name=serializer.validated_data['name'])

        return Response(data={'director_id': director.id}, status=status.HTTP_201_CREATED)


class DirectorDetailView(RetrieveUpdateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        director = self.get_object()
        serializer = self.get_serializer(director, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        director = self.get_object()
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def directors_list_create_api_view(request):
#     if request.method == 'GET':
#         directors = Director.objects.prefetch_related('movies').all()
#         data = DirectorSerializer(directors, many=True).data
#         return Response(data=data)
#
#     elif request.method == 'POST':
#         serializer = DirectorSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data=serializer.errors)
#
#         director = Director.objects.create(
#             **request.data
#         )
#         return Response(data={'director_id': director.id},
#                         status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def directors_detail_api_view(request, id):
#     try:
#         directors = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(
#             status=status.HTTP_404_NOT_FOUND,
#             data={"detail": "Director not found"}
#         )
#
#     if request.method == 'GET':
#         data = DirectorSerializer(directors).data
#         return Response(data=data)
#
#     elif request.method == 'PUT':
#         serializer = DirectorValidationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         directors.name = serializer.validated_data.get('name')
#         directors.save()
#         return Response(data=DirectorSerializer(directors).data,
#                         status=status.HTTP_201_CREATED)
#
#     else:
#         directors.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class MovieListView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        serializer = MovieValidationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        movie = Movie.objects.create(title=serializer.validated_data['title'],
                                     description=serializer.validated_data['description'],
                                     duration=serializer.validated_data['duration'],
                                     director_id=serializer.validated_data['director_id'])
        return Response(data={'movie_id': movie.id},
                        status=status.HTTP_201_CREATED)


class MovieDetailView(RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = self.get_serializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def movies_list_api_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         data = MovieSerializer(movies, many=True).data
#         return Response(data=data)
#
#     elif request.method == 'POST':
#         serializer = MovieValidationSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data=serializer.errors)
#         movie = Movie.objects.create(
#             **request.data
#         )
#         return Response(data={'movie_id': movie.id},
#                         status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail_api_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(
#             status=status.HTTP_404_NOT_FOUND,
#             data={"detail": "Director not found"}
#         )
#
#     if request.method == 'GET':
#         data = MovieSerializer(movie).data
#         return Response(data=data)
#
#     elif request.method == 'PUT':
#         serializer = MovieValidationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         movie.title = serializer.validated_data.get('title')
#         movie.description = serializer.validated_data.get('description')
#         movie.duration = serializer.validated_data.get('duration')
#         movie.director_id = serializer.validated_data.get('director_id')
#         movie.save()
#         return Response(data=MovieSerializer(movie).data,
#                         status=status.HTTP_201_CREATED)
#
#     else:
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewListView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        serializer = ReviewValidationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        review = Review.objects.create(text=serializer.validated_data['text'],
                                       movie_id=serializer.validated_data['movie_id'],
                                       stars=serializer.validated_data['stars']
                                       )
        return Response(data={'review_id': review.id},
                        status=status.HTTP_201_CREATED)


class ReviewDetailView(RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        review = self.get_object()
        serializer = self.get_serializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        review = self.get_object()
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def review_list_create_api_view(request):
#     if request.method == 'GET':
#         review = Review.objects.all()
#         data = ReviewSerializer(review, many=True).data
#         return Response(data=data)
#
#     elif request.method == 'POST':
#         serializer = ReviewValidationSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data=serializer.errors)
#         review = Review.objects.create(
#             **request.data
#         )
#         return Response(data={'review_id': review.id},
#                         status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(
#             status=status.HTTP_404_NOT_FOUND,
#             data={"detail": "Review not found"}
#         )
#     if request.method == 'GET':
#         data = ReviewSerializer(review).data
#         return Response(data=data)
#
#     elif request.method == 'PUT':
#         serializer = ReviewValidationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         print(serializer.validated_data)
#
#         review.text = serializer.validated_data.get('text')
#         review.movie_id = serializer.validated_data.get('movie_id')
#         review.stars = serializer.validated_data.get('stars')
#         review.save()
#
#         return Response(data=ReviewSerializer(review).data,
#                         status=status.HTTP_201_CREATED)
#
#     else:
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def review_movie_api_view(request):
#     movies = Movie.objects.select_related('director').prefetch_related('reviews').all()
#     data = MovieReviewSerializer(movies, many=True).data
#     return Response(data=data)
