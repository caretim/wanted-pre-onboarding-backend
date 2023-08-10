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
    create = serializers.SerializerMethodField()


    def get_create(self, validated_data):
        password =bcypt_password(validated_data['password'])
        user = (User.objects.create(
                email =validated_data['email'],
                password =password.decode())) # DB저장 전 decode
        user.save()
        print('저장됨')
        return user
    
    class Meta:
        model = User
        fields =["email","password",'create']





#로그인확인
class UserSerializer(serializers.ModelSerializer):
    email = CustomMailField(required =True)
    password = PasswordField(required =True)
    login = serializers.SerializerMethodField()

    def get_login(self,obj):
        login = 0
        context ='로그인 실패'
        if User.objects.filter(email=obj['email']).exists():
            user =User.objects.get(email=obj['email'])
            user_password  =  user.password
            if bcrypt.checkpw(obj['password'].encode('utf-8'),user_password.encode('utf-8')):
                login= 1 # 로그인성공
                context = '로그인 성공'
                data = {
                'login' :login ,
                'context' : context,
                'email':user.email}

                return data

                
            else:
                login= 0 # 비밀번호 일치하지않음
                context = '비밀번호가 일치하지 않습니다.'
                data = { 'login' : login,
                    'context' :context }
        else:
            login=0 # 아이디가 존재하지않음
            context  = '아이디가 존재하지 않습니다.'
            data = { 'login' : login,
                    'context' :context }
        return data


    class Meta:
        model = User
        fields = ("email", "password",'login')

            

#유저 로그인 , 첫 로그인시 토큰 발급.
# class UserLogin(APIView):
#     serializer_class =UserSerializer
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