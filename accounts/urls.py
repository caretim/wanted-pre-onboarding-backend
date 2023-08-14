
from django.urls import path, include
from . import views
from rest_framework import urls
from rest_framework_simplejwt.views import TokenVerifyView,TokenRefreshView

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns =[
    path('signup/', views.UserSignup.as_view(),name='signup'),
    path('login/', views.UserLogin.as_view(),name='login'),
    path('refresh/', TokenRefreshView.as_view()),
    path('verify/', TokenVerifyView.as_view()),
]
 

