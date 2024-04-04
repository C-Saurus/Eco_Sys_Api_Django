from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError
from user.models import BlackList
from datetime import datetime


def checkAuthToken(token):
    try:
        decoded_access_token = AccessToken(token)
    except TokenError:
        return "Invalid access token"
    if decoded_access_token["exp"] < datetime.now().timestamp():
        BlackList.objects.create(token=token)
        return "Access token has expired"
    tokenExpired = BlackList.objects.filter(token=token)
    if len(tokenExpired) > 0:
        return "Access token has expired"
    else:
        return "OK"
