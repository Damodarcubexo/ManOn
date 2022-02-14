from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.GetAPI.as_view()),
    path('register/', views.RegisterAPI.as_view(), name="register"),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('SentMailView/', views.SentMailView.as_view()),
    path('ResetPasswordview/', views.ResetPasswordview.as_view()),
    path('otp/', views.OtpVerification.as_view()),
    path('update/<int:pk>/', views.ProfileUpdate.as_view()),
]
