from django.urls import path
from . import views

urlpatterns = [
    path('call_data/', views.call_data, name='call_data'),
    path('index_list/', views.index_list, name='index_list'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/recommend_users/', views.recommend_users, name='recommend_users'),
]