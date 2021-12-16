from django.shortcuts import get_object_or_404, get_list_or_404
from django.http.response import JsonResponse
from .models import Review, Comment
from .serializers import ReviewSerializer, CommentSerializer
from movies.models import Movie
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['GET'])
@permission_classes([AllowAny])
def index(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create(request):
    serializer = ReviewSerializer(data=request.data) 
    movie_title = request.data.get('movie_title')
    movie = get_object_or_404(Movie, title=movie_title)

    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    # 리뷰 상세
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # 리뷰 수정
    elif request.method == 'PUT':
        movie_title = request.data.get('movie_title')
        movie = get_object_or_404(Movie, title=movie_title)

        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # 리뷰 삭제
    else:
        review.delete()
        return Response(data='delete success', status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def comment_creat(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_serializer = CommentSerializer(data=request.data)

    if comment_serializer.is_valid():
        comment_serializer.save(review=review, user=request.user)
        # print(comment_serializer)
        return Response(comment_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([AllowAny])
def review_comments(request):
    # 댓글 조회
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def comment_update_delete(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    # 댓글 수정
    if request.method == 'PUT':
        comment_serializer = CommentSerializer(instance=comment, data=request.data)
        if comment_serializer.is_valid(raise_exception=True):
            comment_serializer.save(user=request.user, review=review)
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
    
    
    # 댓글 삭제
    else:
        comment.delete()
        return Response(data='delete success', status=status.HTTP_204_NO_CONTENT)
