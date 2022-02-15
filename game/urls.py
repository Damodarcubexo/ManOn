from django.urls import path
from . import views

urlpatterns = [
    path('getgame/', views.GameView.as_view()),
    path('search/', views.SearchPlayer.as_view()),
]
