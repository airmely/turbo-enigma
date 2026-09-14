from django.db import models

from apps.balance.choices import Currency, TransactionAction, TransactionStatus
from apps.common.models import TimeStampedModel


class Balance(TimeStampedModel):
    owner = models.OneToOneField(
        to="users.User",
        on_delete=models.CASCADE,
    )
    amount = models.PositiveBigIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    currency = models.CharField(
        choices=Currency.choices,
        default=Currency.RUB,
        max_length=3,
    )

    def __str__(self):
        return f"{self.amount} {self.currency}"


class Transaction(TimeStampedModel):
    sender = models.ForeignKey(
        to="users.User",
        on_delete=models.CASCADE,
        related_name="sender_balance",
    )
    receiver = models.ForeignKey(
        to="users.User",
        on_delete=models.CASCADE,
        related_name="receiver_balance",
    )
    amount = models.PositiveBigIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    action = models.CharField(
        choices=TransactionAction.choices,
        default=TransactionAction.DEPOSIT,
        max_length=10,
    )
    status = models.CharField(
        choices=TransactionStatus.choices,
        default=TransactionStatus.PENDING,
        max_length=10,
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.sender} -> {self.receiver} send {self.amount} with status: {self.status}"
