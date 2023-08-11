
from django.contrib.auth import get_user_model,authenticate,login
from .serializers import UserSignupSerializer,UserSerializer

from rest_framework import status,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny 

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,RefreshToken


# Create your views here.

User= get_user_model()

#유저 회원가입

class UserSignup(APIView):
    serializer_class =UserSignupSerializer
    permission_classes = [AllowAny]
    
    def post(self,request, *args, **kwargs):
        serializer = UserSignupSerializer
        serializer =serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        user =User.objects.get(email=data['email'])
        token = TokenObtainPairSerializer.get_token(user)
        refresh_token = str(token)
        access_token  = str(token.access_token)
        context = Response({
                "user": user.email,
                'password' : user.password,
                "refresh_token": refresh_token,
                "access_token" :access_token }
                ,status=status.HTTP_200_OK)
        return context



class UserLogin(APIView):
    serializer_class =UserSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer
        serializer =serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data['login']
        if data['login'] == 1: # 로그인 성공
            user =User.objects.get(email=data['email'])
            #토큰 재발행
            token = RefreshToken.for_user(user)
            refresh_token = str(token)
            access_token  = str(token.access_token)
            context = Response(
                {
                    "user": data['email'],
                    "message": "로그인성공",
                    "token": {
                        "access_token": access_token,
                        "refresh_token": refresh_token
                    },
                },
                status=status.HTTP_200_OK
            )
        else: # 로그인 실패
            context =(
            Response(
                {'message' : data['context']}))
        return  context


