from django.shortcuts import render
from .models import User
from .serializers import UserSignupSerializer
from rest_framework.decorators import api_view

from rest_framework import generics
# Create your views here.




class UserSignup(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class =UserSignupSerializer


# @api_view
# def signup(request):
