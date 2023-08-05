from rest_framework import serializers
from .models import User
from .customfield import CustomMailField ,PasswordField
import bcrypt

password = '1234'.encode('utf-8')

class UserSignupSerializer(serializers.Serializer):
        email = CustomMailField(required =True)
        password = PasswordField(required =True)
        # password_check =PasswordField(required=True)

        def create(self, validated_data):
            password =validated_data['password']
            hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
            validated_data['password'] = hashed_password
            user = User.objects.create(**validated_data)
            return user



