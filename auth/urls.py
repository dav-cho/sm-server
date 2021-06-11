from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    RegisterUserView,
    LoginUserView,
    LogoutUserView,
)

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
]
