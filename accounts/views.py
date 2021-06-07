from django.contrib.auth import authenticate, login
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import AuthenticationFailed

from .serializers import UserSerializer, RegisterSerializer
from .models import User


class ListUsers(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Register(APIView):
    def post(self, req):
        serializer = RegisterSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        user = serializer.save()
        serializer.data["response"] = "Successfully registered a new user."
        # serializer.data["email"] = user.email
        # serializer.data["username"] = user.username
        return Response(serializer.data)


class Login(APIView):
    def post(self, req):
        email = req.data["email"]
        password = req.data["password"]

        user = authenticate(req, email=email, password=password)
        # user = User.objects.filter(email=email).first()

        if user is not None:
            login(req, user)

        if user is None:
            raise AuthenticationFailed("User not found.")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password")

        return Response({"message": "success"})
