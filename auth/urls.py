from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegisterUser, Login, Logout

urlpatterns = [
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
]
