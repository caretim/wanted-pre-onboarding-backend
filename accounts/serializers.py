from rest_framework import serializers
from .models import User



def  UserValidata(value):
    print(value)
    if '@' not in value['email']:
            raise serializers.ValidationError('@를 포함해주세요')
    elif len(value['password']) < 8:
            raise serializers.ValidationError('비밀번호를 8자 이상으로 만들어주세요')
    else:
        return value

    



class UserSerializer(serializers.ModelSerializer):
    def create(self, UserValidata):
        # print(self)
        # print(UserValidata)
        return super().create(UserValidata)
    
    #유효성검사 
    # 1. 가입시 이메일에 @ 포함,
    # 2. 비밀번호 생성 시 8자 이상으로 생성 
    # def validate_email(self, value):
    #     if '@' not in value:
    #         raise serializers.ValidationError('@를 포함해주세요')
    #     else:
    #         return value
    # def validate_password(self, value):
    #     if len(value) < 8:
    #         raise serializers.ValidationError('비밀번호를 8자 이상으로 만들어주세요')
    #     else:
    #         return value
    class Meta:
        model = User
        fields = ['email','password']

