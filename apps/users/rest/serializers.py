from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator
from rest_framework import serializers

from apps.balance.models import Balance
from apps.users.validators import UniqueMailLowerValidator

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for user creation
    """

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "username",
        )
        extra_kwargs = {
            "password": {"validators": [validate_password], "write_only": True},
            "email": {
                "validators": [
                    EmailValidator,
                    UniqueMailLowerValidator(
                        queryset=User.objects.all(),
                        message="user with this email already exists.",
                    ),
                ]
            },
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            username=validated_data["username"],
        )
        user.save()
        return user


class UserCompleteSerializer(serializers.ModelSerializer):
    """
    Complete serializer for user.
    """

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "balance",
        )
        read_only_fields = (
            "id",
            "email",
            "username",
        )
