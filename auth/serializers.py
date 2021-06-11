from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from accounts.models import User
from api.serializers import PostSerializer, CommentSerializer, ReactionSerializer

from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.settings import api_settings


class RegisterUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password",
            "confirm_password",
            "id",
            "created",
            "last_login",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User(email=validated_data["email"], username=validated_data["username"])
        password = validated_data["password"]
        confirm_password = validated_data["confirm_password"]
        if password != confirm_password:
            raise ValidationError({"password": "Passwords do not match."})
        user.set_password(password)
        user.save()
        return user


class LoginUserSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        print("~ user", user)

        token = super(LoginUserSerializer, cls).get_token(user)
        # need?
        token["id"] = user.id
        token["username"] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        # data["refresh"] = str(refresh)
        # data["access"] = str(refresh.access_token)
        data["user"] = {
            "id": self.user.id,
            "email": self.user.email,
            "username": self.user.username,
            "last_login": self.user.last_login,
            "created": self.user.created,
            # "posts": user.posts,
            # "comments": user.comments,
            # "reactions": user.reactions,
        }

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class VerifyUserSerializer(serializers.ModelSerializer):
    posts = PostSerializer()
    comments = CommentSerializer()
    reactions = ReactionSerializer()

    class Meta:
        model = User
        exclude = ["password", "is_admin", "is_superuser", "is_staff"]


# TODO: add update / delete logic
class ChangeUserPasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    confirm_new_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ("old_password", "new_password", "confirm_new_password")

        def validate(self, attrs):
            if attrs["new_password"] != attrs["old_password"]:
                raise ValidationError({"password": "Passwords do not match."})
            return attrs
