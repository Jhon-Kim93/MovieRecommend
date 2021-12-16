from django.shortcuts import get_object_or_404, get_list_or_404
from django.http.response import JsonResponse
from .models import Movie, Genre
from .tests import TMDBHelper
from .serializers import MovieSerializer, GenreSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
import requests


@api_view(['GET'])
def call_data(request):
    # save -> admin 관리자만 허용 / 실행 시 전체 db 삭제 후 다시 저장
    # if request.user == 'admin':
    tmdb_helper = TMDBHelper(TMDBHelper.api_key)
    request_url = tmdb_helper.get_request_url(region='KR', language='ko')
    genre_url = tmdb_helper.get_genre_url(region='KR', language='ko')
    # if get_list_or_404(Movie):
    #     movies = get_list_or_404(Movie)
    #     serializer_all = MovieSerializer(movies, many=True)
    
    # 장르 목록 수집 및 저장
    data_genre = []
    tmp = requests.get(genre_url).json()
    data_genre.append(tmp.get('genres'))
    for i in range(len(data_genre[0])):
        serializer = GenreSerializer(data=data_genre[0][i])
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    # 영화 목록 수집 및 저장
    data = []
    for i in range(1, 11):
        request_url += f'&page={i}'
        tmp = requests.get(request_url).json()
        for j in range(20):
            data.append(tmp.get('results')[j])
    
    for i in range(len(data)):
        serializer = MovieSerializer(data=data[i])
        if serializer.is_valid(raise_exception=True):
            movie = serializer.save()

        # 중계 테이블 추가
        g_ids = [Genre.objects.get(pk=g_id) for g_id in data[i].get('genre_ids')]    
        for genre in g_ids:
            movie.genre_ids.add(genre)


@api_view(['GET'])
@permission_classes([AllowAny])
def index_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def recommend_users(request, movie_pk):

    # 생성, 삭제
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.recommend_users.filter(pk=user.pk).exists():
            movie.recommend_users.remove(user)
            is_recommended = False
        else:
            movie.recommend_users.add(user)
            is_recommended = True
        context = {
            'is_recommended': is_recommended,
            'recommend_cnt': movie.recommend_users.count(),
        }
        return JsonResponse(context)


