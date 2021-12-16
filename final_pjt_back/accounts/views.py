from django.http import response
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from django.http.response import JsonResponse
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer, UserProfileSerializer, UserLoginSerializer
from .models import User
from movies.serializers import MovieSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def login(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserLoginSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    username = request.data.get('username')
    if username == 'admin':
        return Response({'error': '관리자 계정 생성 불가'}, status=status.HTTP_400_BAD_REQUEST)

    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
	
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def profile(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = UserSerializer(person)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([AllowAny])
def profile_update(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)

    # first_name = request.data.get('first_name')
    # last_name = request.data.get('last_name')
    # email = request.data.get('email')

    serializer = UserProfileSerializer(instance=person, data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def secret_friend(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    user = request.user
    if person != user:
        if person.secret_followers.filter(pk=user.pk).exists():
            person.secret_followers.remove(user)
            is_followed = False
        else:
            person.secret_followers.add(user)
            is_followed = True
    context = {
        'is_followed': is_followed,
        # 'secret_following_nums': person.secret_friends.count(),
        'secret_follower_nums': person.secret_followers.count()
    }
    return JsonResponse(context)


@api_view(['GET'])
@permission_classes([AllowAny])
def recommend_movies(request, username):
    user = get_object_or_404(User, username=username)

    recommend_movies = list(user.recommend_movies.all().values('id', 'title', 'poster_path', 'vote_average'))
    context= {
        'recommend_movies': recommend_movies
    }
    return JsonResponse(context)

@api_view(['GET'])
def random_recommend_movies(request):
# (랜덤영화추천목록) -> 지금 로그인한 사람의 db에서 내가 비밀친구 맺은 user를 조회해서 user의 추천영화를 가져온다 
    secret_friends_recommend_movies = set()
    secret_friends = request.user.secret_friends.all()

    for secret_friend in secret_friends:
        recommended_movies = secret_friend.recommend_movies.all()
        for recommended_movie in recommended_movies:
            secret_friends_recommend_movies.add(recommended_movie)

    serializer = MovieSerializer(list(secret_friends_recommend_movies), many=True)
    return Response(serializer.data)
