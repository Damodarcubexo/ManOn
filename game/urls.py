from django.urls import path
from . import views

urlpatterns = [
      path('getgame/<id>', views.GameView.as_view()),
]

