from django.db import models
from  django.contrib.auth.models import AbstractBaseUser,BaseUserManager





class UserManager(BaseUserManager):
    def create_user(self,email):
        user = self.model(
            email=email,
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "email"