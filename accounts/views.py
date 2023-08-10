
from django.contrib.auth import get_user_model,authenticate,login
from .serializers import UserSignupSerializer,UserSerializer

from rest_framework import status,generics
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



# Create your views here.

User= get_user_model()

#유저 회원가입

class UserSignup(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class =UserSignupSerializer



class UserLogin(APIView):
    serializer_class =UserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer
        serializer =serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data['login']
        if data['login'] == 1:
            user =User.objects.get(email=data['email'])
            token = TokenObtainPairSerializer.get_token(user)

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
            context.set_cookie("access_token", access_token, httponly=True)
            context.set_cookie("refresh_token", refresh_token, httponly=True)
        else:
            context =(
            Response(
                {'message' : data['context']}))
        return  context


