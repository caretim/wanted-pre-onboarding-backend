from rest_framework import serializers
from .models import User
from .customfield import CustomMailField ,PasswordField


class UserSignupSerializer(serializers.Serializer):
        email = CustomMailField(required =True)
        password = PasswordField(required =True)
        # password_check =PasswordField(required=True)

        def create(self, validated_data):
            user = User.objects.create(**validated_data)
            return user



