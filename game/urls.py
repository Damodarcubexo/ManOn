from django.urls import path
from . import views

urlpatterns = [
    path('history_save/<int:pk>', views.History.as_view()),

]