
from django.contrib.auth import get_user_model
from .serializers import UserSignupSerializer,UserLoginSerializer

from rest_framework import status,generics
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



# Create your views here.



#유저 회원가입

class UserSignup(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class =UserSignupSerializer


class UserLogin(GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class =UserLoginSerializer

#유저 로그인 , 첫 로그인시 토큰 발급.
# class UserLogin(APIView):
#     serializer_class =UserLoginSerializer
#     def post(self,request):
#         serializer = self.serializer_class(data=request.data)
#         print(serializer)
#         if serializer.is_valid(raise_exception=True):
#             # token = TokenObtainPairSerializer.get_token(user)
#             # refresh_token = str(token)
#             # access_token = str(token.access_token)
#             # context = { {
#             #         "user": serializer.data,
#             #         "message": "회원가입완료",
#             #         "token": {
#             #             "access": access_token,
#             #             "refresh": refresh_token,
#             #         },
#             #     }, }
#         # return Response(context, status=status.HTTP_200_OK)
#             return {'aa'}