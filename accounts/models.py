from django.db import models
from  django.contrib.auth.models import AbstractBaseUser,BaseUserManager





class UserManager(BaseUserManager):
    def create_user(self,email):
        user = self.model(
            email=email,
        )
        return user


class User(AbstractBaseUser):
    email = models.CharField(max_length=30, unique=True, null=False, blank=False)
    USERNAME_FIELD = "email"