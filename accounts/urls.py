from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ListUsers, Register, Login

urlpatterns = [
    path("", ListUsers.as_view(), name="users"),
    path("register/", Register.as_view(), name="register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]
