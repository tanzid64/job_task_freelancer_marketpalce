from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenVerifyView,
)
from accounts.views import UserLoginView, UserTokenRefreshView

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/login/", UserLoginView.as_view(), name="login"),
    path("auth/token/refresh/", UserTokenRefreshView.as_view(), name="token-refresh"),
    path("auth/token/verify/", TokenVerifyView.as_view(), name="token-verify"),
]
