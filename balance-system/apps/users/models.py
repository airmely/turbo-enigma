from django.contrib.auth.models import AbstractUser

from apps.common.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    pass
