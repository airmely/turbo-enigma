from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator
from rest_framework import serializers

from apps.balance.rest.serializers import BalanceSerializer
from apps.users.validators import UniqueMailLowerValidator

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for user creation
    """

    balance = BalanceSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "username",
            "balance",
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

    balance = BalanceSerializer(read_only=True)

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
