from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('random_recommend_movies/',views.random_recommend_movies, name='random_recommend_movies'),
    path('<int:user_pk>/', views.profile, name='profile'),
    path('<int:user_pk>/update/', views.profile_update, name='profile_update'),
    path('<username>/login/', views.login, name='login'),
    path('<username>/secret_friend/', views.secret_friend, name='secret_friend'),
    path('<username>/recommend_movies/', views.recommend_movies, name='recommend_movies'),
    path('api/token/', obtain_jwt_token),
]