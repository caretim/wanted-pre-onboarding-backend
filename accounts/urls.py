
from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    path('signup/', views.UserSignup.as_view()),
    path('login/', views.UserLogin.as_view()),
    path('logout/', views.UserSignup.as_view()),
 ]

