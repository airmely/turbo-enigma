from django.db import models


class Currency(models.TextChoices):
    RUB = "₽", "₽"
    USD = "$", "$"


class TransactionAction(models.TextChoices):
    DEPOSIT = "deposit", "Deposit"
    WITHDRAW = "withdraw", "Withdraw"


class TransactionStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    COMPLETED = "completed", "Completed"
    FAILED = "failed", "Failed"
