from rest_framework import serializers
from .models import Movie, Genre
from django.contrib.auth import get_user_model

class MovieSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username',)

    recommend_users = UserSerializer(many=True, read_only=True,)

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name',)

    genre_ids = GenreSerializer(many=True, read_only=True,)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_date', 'vote_average',
            'overview', 'poster_path', 'recommend_users', 'genre_ids',)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name',)