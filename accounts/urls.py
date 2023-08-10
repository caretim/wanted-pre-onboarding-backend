
from django.urls import path, include
from . import views
from rest_framework import urls
from rest_framework_simplejwt.views import TokenVerifyView,TokenRefreshView
urlpatterns =[
    path('signup/', views.UserSignup.as_view()),
    path('login/', views.UserLogin.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verify/', TokenVerifyView.as_view())

 ]

