from rest_framework import serializers

from apps.balance.models import Balance, Transaction


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = "__all__"


class TopUpBalanceSerializer(serializers.Serializer):
    amount = serializers.IntegerField()

    class Meta:
        fields = ("amount",)

    def validate_amount(self, amount):  # noqa
        if amount <= 0:
            raise serializers.ValidationError("The sum must be positive.")
        return amount


class BalanceDetailSerializer(serializers.Serializer):
    """Used for documentation only swagger"""

    balance = serializers.IntegerField()

    class Meta:
        fields = ("balance",)


class TransactionHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"


class SendAmountUserToUserSerializer(serializers.Serializer):
    amount = serializers.IntegerField()

    def validate_amount(self, value):  # noqa
        if value <= 0:
            raise serializers.ValidationError("The sum must be positive.")
        return value
