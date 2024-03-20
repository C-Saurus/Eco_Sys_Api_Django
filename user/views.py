from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from .models import BlackList
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework import status
from django.utils import timezone


@api_view(["POST"])
def register(request):
    email = request.data.get("email")
    username = request.data.get("username")
    password = make_password(request.data.get("password"))
    age = request.data.get("age")
    phone = request.data.get("phone")

    if email and username and password and age and phone:
        user = User.objects.create_user(
            email=email, username=username, password=password
        )
        user.age = age
        user.phone = phone
        user.save()
        return Response({"message": "User created successfully"}, status=201)
    else:
        return Response({"error": "All fields are required"}, status=400)


@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = make_password(request.data.get("password"))

    user = authenticate(request, username=email, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        return Response(
            {"access_token": access_token, "refresh_token": refresh_token}, status=200
        )
    else:
        return Response({"error": "Invalid credentials"}, status=401)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    token = request.data.get("access_token")
    BlackList.objects.create(token=token)
    return Response({"message": "Logged out successfully"}, status=200)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUser(request, id):
    access_token = request.META.get("HTTP_AUTHORIZATION", "").split(" ")[1]
    try:
        decoded_access_token = AccessToken(access_token)
    except TokenError:
        return Response(
            {"error": "Invalid access token"}, status=status.HTTP_401_UNAUTHORIZED
        )

    if decoded_access_token["exp"] < timezone.now():
        BlackList.objects.create(token=access_token)
        return Response(
            {"error": "Access token has expired"}, status=status.HTTP_401_UNAUTHORIZED
        )

    user_instance = User.objects.get(id=id)
    serializer = UserSerializer(user_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)
