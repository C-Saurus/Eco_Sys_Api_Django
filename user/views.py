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
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(["POST"])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")
    age = request.data.get("age")
    phone = request.data.get("phone")
    if not username:
        return Response(
            {"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    if not email:
        return Response(
            {"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    if not password:
        return Response(
            {"error": "Password is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    # Kiểm tra xem đã có người dùng với username hoặc email này chưa
    listUser = User.objects.filter(username=username)
    print(listUser)
    if len(listUser) > 0:
        return Response(
            {"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST
        )
    listUser = User.objects.filter(email=email)
    if len(listUser) > 0:
        return Response(
            {"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST
        )
    listUser = User.objects.filter(phone=phone)
    if len(listUser) > 0:
        return Response(
            {"error": "Phone number already exists"}, status=status.HTTP_400_BAD_REQUEST
        )
    print("DMM")
    # Tạo mật khẩu đã được mã hóa
    hashed_password = make_password(password, username)

    # Tạo người dùng mới và lưu vào cơ sở dữ liệu
    new_user = User.objects.create(
        username=username, password=hashed_password, email=email, age=age, phone=phone
    )
    new_user.save()

    return Response(
        {"message": "User registered successfully"}, status=status.HTTP_201_CREATED
    )


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = make_password(request.data.get("password"), username)
    user = authenticate(request, username=username, password=password)
    print("user", user)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        return Response(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user_id": user.id,
            },
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    access_token = request.META.get("HTTP_AUTHORIZATION", "").split(" ")[1]
    try:
        decoded_access_token = AccessToken(access_token)
    except TokenError:
        return Response(
            {"error": "Invalid access token"}, status=status.HTTP_401_UNAUTHORIZED
        )
    if decoded_access_token["exp"] < datetime.now().timestamp():
        BlackList.objects.create(token=access_token)
        return Response(
            {"error": "Access token has expired"}, status=status.HTTP_401_UNAUTHORIZED
        )
    tokenExpired = BlackList.objects.get(token=access_token)
    print(tokenExpired)
    if tokenExpired is not None:
        return Response(
            {"error": "Access token has expired"}, status=status.HTTP_401_UNAUTHORIZED
        )
    BlackList.objects.create(token=access_token)
    return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)


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
    if decoded_access_token["exp"] < datetime.now().timestamp():
        BlackList.objects.create(token=access_token)
        return Response(
            {"error": "Access token has expired"}, status=status.HTTP_401_UNAUTHORIZED
        )
    tokenExpired = BlackList.objects.get(token=access_token)
    if tokenExpired is not None:
        return Response(
            {"error": "Access token has expired"}, status=status.HTTP_401_UNAUTHORIZED
        )
    user_instance = User.objects.get(id=id)
    serializer = UserSerializer(user_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)
