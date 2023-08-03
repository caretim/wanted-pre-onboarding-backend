from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return super().create(validated_data)
    
    def validate_email(self, value):
        if '@' not in value:
            raise serializers.ValidationError('@를 포함해주세요')
        else:
            return value
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('비밀번호를 8자 이상으로 만들어주세요')
        else:
            return value
    class Meta:
        models = User
        fields = ['email','password']

