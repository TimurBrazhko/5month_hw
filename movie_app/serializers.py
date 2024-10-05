from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movie_count'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director review_list rating '.split()
