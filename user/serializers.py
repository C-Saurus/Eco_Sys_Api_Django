from rest_framework import serializers
from .models import User, BlackList
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
