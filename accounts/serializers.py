from datetime import datetime
from djoser.serializers import UserCreateSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("email", "username", "name", "password", "role")


class UserLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Calculate expiration time in seconds
        access_token_lifetime = api_settings.ACCESS_TOKEN_LIFETIME
        refresh_token_lifetime = api_settings.REFRESH_TOKEN_LIFETIME
        data["expires_in"] = {
            "access": int((access_token_lifetime).total_seconds()),
            "refresh": int((refresh_token_lifetime).total_seconds()),
        }
        return data

class UserTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Calculate expiration time in seconds
        access_token_lifetime = api_settings.ACCESS_TOKEN_LIFETIME
        refresh_token_lifetime = api_settings.REFRESH_TOKEN_LIFETIME
        data["expires_in"] = {
            "access": int((access_token_lifetime).total_seconds()),
            "refresh": int((refresh_token_lifetime).total_seconds()),
        }
        return data
