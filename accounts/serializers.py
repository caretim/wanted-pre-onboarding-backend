from rest_framework import serializers
from django.contrib.auth import get_user_model
from .customfield import CustomMailField ,PasswordField
import bcrypt

User= get_user_model()


# customfield.py를 통해 특정 유효성 검사만 되는 필드 생성,
# 커스텀 유효성검사를 통해 필드 유효성 검사,
# 이메일에서 @ 외의 모든 유효성검사 제외
# 패스워드에서 8자이상 제한 모든 유효성검사 제외 


#회원가입
class UserSignupSerializer(serializers.Serializer):
      email = CustomMailField(required =True)
      password = PasswordField(required =True)
      class Meta:
            model = User
            fields =["email","password"]
            

      def create(self, validated_data):
            password =validated_data['password']
            # bcrypt를 통해 패스워드 해싱  
            hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
            validated_data['password'] = hashed_password
            user = User.objects.create(**validated_data)
            return user


#회원가입 필드와 meta 상속, post기능만
class UserLoginSerializer(UserSignupSerializer):
      email = CustomMailField(required =True)
      password = PasswordField(required =True)
      class Meta:
            model = User
            fields =["email","password"] 

      def post(self, validated_data):
            password =validated_data['password']
            # bcrypt를 통해 패스워드 해싱  
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            validated_data['password'] = hashed_password
            try:
                user = User.objects.get(**validated_data)
                return user
            except:
                  context={
                        'message': '유효하지 않은 메세지입니다.'
                  }
                  return context
            
#로그인 
class UserLoginSerializer(serializers.Serializer):
        email = CustomMailField(required =True)
        password = PasswordField(required =True,write_only=True)
        class Meta:
              model = User
              fields =["email",'password']


            

