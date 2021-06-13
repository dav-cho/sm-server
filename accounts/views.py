from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User
from .serializers import UserSerializer, CurrentUserSerializer


class UserListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = "username"


class CurrentUserView(APIView):
    user_model = get_user_model()

    def post(self, req):
        header = JWTAuthentication.get_header(self, request=req)
        raw_token = JWTAuthentication.get_raw_token(self, header=header)
        token = AccessToken(token=raw_token)
        user_obj = JWTAuthentication.get_user(self, validated_token=token)
        user = User.objects.get(pk=user_obj.id)
        serializer = CurrentUserSerializer(instance=user)
        data = serializer.data

        return Response(data)


class ProfileView(APIView):
    permission_classes = [AllowAny]
    # serializer_class = UserProfileSerializer

    def post(self, req):
        pass
