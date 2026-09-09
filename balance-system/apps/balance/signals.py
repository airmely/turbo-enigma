from typing import Any

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.balance.models import Balance

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_balance(
    sender,
    instance: "Balance",
    created: Any,
    **kwargs: dict[..., Any],
) -> None:
    """When creating a new user, a balance is automatically created."""
    if created:
        Balance.objects.create(owner=instance)
