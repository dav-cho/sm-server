from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, req):
        email = req.data["email"]
        password = req.data["password"]
        user = authenticate(req, email=email, password=password)
        if user is None:
            raise AuthenticationFailed("User not found.")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password")
        login(req, user)
        return Response("Successfully logged in.")


class Logout(APIView):
    permission_classes = [AllowAny]

    def post(self, req):
        logout(req)
        return Response("Successfully logged out.")


class BlacklistRefreshToken(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
