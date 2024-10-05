from django.db import models


class Balance(models.Model):
    owner = models.OneToOneField(
        to="users.User",
        on_delete=models.CASCADE,
    )
    amount = models.PositiveSmallIntegerField(
        default=0,
        blank=False,
        null=False,
    )


class Transaction(models.Model):
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

    class Meta:
        ordering = ("created_at",)
