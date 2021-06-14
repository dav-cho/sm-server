from django.contrib.auth.models import update_last_login
from rest_framework.serializers import ModelSerializer, ValidationError, CharField
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from accounts.models import User
from accounts.serializers import UserSerializer


class RegisterUserSerializer(ModelSerializer):
    confirm_password = CharField(required=True, write_only=True)

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
        token = super(LoginUserSerializer, cls).get_token(user)
        token["id"] = user.id
        token["username"] = user.username

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        user = UserSerializer(instance=self.user)
        data["user"] = user.data
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data


# TODO:
class ChangeUserPasswordSerializer(ModelSerializer):
    old_password = CharField(required=True, write_only=True)
    new_password = CharField(required=True, write_only=True)
    confirm_new_password = CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ("old_password", "new_password", "confirm_new_password")

        def validate(self, attrs):
            if attrs["new_password"] != attrs["old_password"]:
                raise ValidationError({"password": "Passwords do not match."})
            return attrs
