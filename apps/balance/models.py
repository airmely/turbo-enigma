from django.db import models


class Balance(models.Model):

    RUB = "₽"
    USD = "$"

    CURRENCY_CHOICES = (
        (RUB, "₽"),
        (USD, "$"),
    )

    owner = models.OneToOneField(
        to="users.User",
        on_delete=models.CASCADE,
    )
    amount = models.PositiveSmallIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES,
        default=RUB,
        max_length=3,
    )

    def __str__(self):
        return f"{self.amount} {self.currency}"


class Transaction(models.Model):

    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"

    ACTIONS_CHOICES = (
        (DEPOSIT, "Deposit"),
        (WITHDRAW, "Withdraw"),
    )

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
    amount = models.PositiveSmallIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    action = models.CharField(
        choices=ACTIONS_CHOICES,
        default=DEPOSIT,
        max_length=10,
    )

    class Meta:
        ordering = ("-created_at",)
