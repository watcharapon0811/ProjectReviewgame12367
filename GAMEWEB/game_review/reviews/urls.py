from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('game/<int:pk>/', views.game_detail, name='game_detail'),
    path('review_game/', views.review_game, name='review_game'),
]
