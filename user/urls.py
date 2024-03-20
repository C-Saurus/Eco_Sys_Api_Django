from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import login, logout, register, getUser

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("<int:id>/", getUser, name="getUser"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
