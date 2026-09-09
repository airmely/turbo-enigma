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
    amount = models.PositiveBigIntegerField(
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

    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

    ACTIONS_CHOICES = (
        (DEPOSIT, "Deposit"),
        (WITHDRAW, "Withdraw"),
    )

    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (COMPLETED, "Completed"),
        (FAILED, "Failed"),
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
    amount = models.PositiveBigIntegerField(
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
    status = models.CharField(
        choices=STATUS_CHOICES,
        default=PENDING,
        max_length=10,
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.sender} -> {self.receiver} send {self.amount} with status: {self.status}"
