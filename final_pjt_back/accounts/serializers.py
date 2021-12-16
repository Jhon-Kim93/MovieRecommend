from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password',)


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'last_name', 'email', )

class UserLoginSerializer(serializers.ModelSerializer):
    class SecretFriendsSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('id', 'username')
    
    secret_friends = SecretFriendsSerializer(many=True, read_only=True,)
    secret_followers = SecretFriendsSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'secret_friends', 'secret_followers')

