from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate
from .customfield import CustomMailField ,PasswordField

import bcrypt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User= get_user_model()


# customfield.py를 통해 특정 유효성 검사만 되는 필드 생성,
# 커스텀 유효성검사를 통해 필드 유효성 검사,
# 이메일에서 @ 외의 모든 유효성검사 제외
# 패스워드에서 8자이상 제한 모든 유효성검사 제외 

#암호 해싱 함수
def bcypt_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    change_password = hashed_password
    return change_password


#회원가입
class UserSignupSerializer(serializers.ModelSerializer):
    email = CustomMailField(required =True)
    password = PasswordField(required =True)
    class Meta:
        model = User
        fields =["email","password"]

    def create(self, validated_data):
        password =bcypt_password(validated_data['password'])
        user = (User(
                email =validated_data['email'],
                password =password))
        user.save()
        return user





#로그인확인
class UserSerializer(serializers.ModelSerializer):
    email = CustomMailField(required =True)
    password = PasswordField(required =True)
    token = serializers.SerializerMethodField()

    def get_token(self,obj):
        Return_Data = False
        if User.objects.filter(email=obj['email']).exists():
            user_password  =  User.objects.get(email=obj['email'])
            if bcrypt.checkpw(user_password.encode('utf-8'),user_password.password):
                Return_Data = True
        print(Return_Data)


    class Meta:
        model = User
        fields = ("email", "password",'token')

            

