from django.apps import AppConfig


class BalanceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.balance"

    def ready(self):
        import apps.balance.signals  # noqa
