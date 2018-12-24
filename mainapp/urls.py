from django.urls import path, re_path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('dev/games/', views.DevGames.as_view(), name='dev_games'),
    path('dev/create_game/', views.CreateGame.as_view(), name='create_game'),
    path('dev/<int:game_id>/dev_game_description/', views.DevGameDescription.as_view(), name='dev_game_description'),
]