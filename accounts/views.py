from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.renderers import JSONRenderer

from .models import User
from .serializers import UserSerializer
from auth.serializers import VerifyUserSerializer

from django.core import serializers


class UserListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetUserDetailsView(APIView):
    permission_classes = [AllowAny]
    user_model = get_user_model()
    serializer_class = VerifyUserSerializer

    def post(self, req):
        token = AccessToken(token=req.data["access"])
        user = JWTAuthentication.get_user(self, validated_token=token)

        # TODO: serialize user object with user serializer?
        user_data = {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "last_login": user.last_login,
            "created": user.created,
            # "posts": user.posts,
            # "comments": user.comments,
            # "reactions": user.reactions,
        }
        return Response(user_data)
