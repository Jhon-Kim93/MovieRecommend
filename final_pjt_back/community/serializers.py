from rest_framework import serializers
from .models import Review, Comment
from django.contrib.auth import get_user_model
from movies.models import Movie


class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username', 'password',)

    user = UserSerializer(read_only=True)

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk', 'title',)
    
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username', 'password',)

    user = UserSerializer(read_only=True)

    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('pk',)
    
    review = ReviewSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'review',)