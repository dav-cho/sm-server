from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User

from .serializers import (
    RegisterUserSerializer,
    LoginUserSerializer,
)

from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


class RegisterUserView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class LoginUserView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = LoginUserSerializer
    # TODO: add GetUserDetail logic from account views
    # - send back user info on login

    def post(self, req, *args, **kwargs):
        serializer = self.get_serializer(data=req.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class LogoutUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, req):
        try:
            refresh_token = req.data["refresh"]
            refresh_token = RefreshToken(refresh_token)
            refresh_token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ChangeUserPasswordView(APIView):
    pass
