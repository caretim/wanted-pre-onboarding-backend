from django.db import models

# Create your models here.
from django.db import models
from  django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    USERNAME_FIELD = "email"