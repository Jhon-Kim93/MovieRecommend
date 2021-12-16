from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:review_pk>/detail_update_delete', views.detail_update_delete, name='detail_update_delete'),
    path('review_comments/', views.review_comments, name='review_comments'),
    path('<int:review_pk>/comments/create/', views.comment_creat, name='comment_creat'),
    path('<int:review_pk>/comments/<int:comment_pk>/update_delete/', views.comment_update_delete, name='comment_update_delete'),
]
