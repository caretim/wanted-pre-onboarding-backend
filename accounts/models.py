from django.db import models
from  django.contrib.auth.models import AbstractBaseUser,BaseUserManager





class UserManager(BaseUserManager):
    def create_user(self,email,password):
        if not email:
            raise ValueError("이메일을 입력해주세요")

        user = self.model(
            email=email,
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    USERNAME_FIELD = "email"