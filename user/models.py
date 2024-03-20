from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    phone = models.TextField(max_length=11, unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}


class BlackList(models.Model):
    token = models.CharField(max_length=100)
