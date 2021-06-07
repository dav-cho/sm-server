from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    # def create(self, validated_data):
    #     password = validated_data.pop("password", None)
    #     user = self.Meta.model(**validated_data)
    #     if password is not None:
    #         user.set_password(password)
    #     user.save()
    #     return user


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "confirm_password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def save(self):
        user = User(
            email=self.validated_data["email"], username=self.validated_data["username"]
        )
        password = self.validated_data["password"]
        confirm_password = self.validated_data["confirm_password"]

        if password != confirm_password:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        user.set_password(password)
        user.save()