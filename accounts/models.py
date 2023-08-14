from django.db import models
from  django.contrib.auth.models import AbstractBaseUser,BaseUserManager





class UserManager(BaseUserManager):
    def create_user(self,email,password):
        user = self.model(
            email=email,
            password= password
        )
        return user
    def create_superuser(self, email, password, **extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,
        )
        superuser.is_staff = True
        superuser.is_admin = True
        superuser.is_active = True
        superuser.is_super = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = "email"

    objects = UserManager()