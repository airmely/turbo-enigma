from django.core.management.base import BaseCommand

from apps.users.models import User


class Command(BaseCommand):
    help = "Creates bank in system"

    def handle(self, *args, **options):

        if User.objects.filter(username="Main bank").exists():
            self.stdout.write(self.style.NOTICE("Main bank already exists"))
            return

        user = User.objects.create(
            username="Main bank",
            email="bankOOOSPb@localhost",
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )

        user.balance.amount += 1_000_000
        user.balance.save()
        user.set_password("123")
        user.save()

        self.stdout.write(
            self.style.SUCCESS(
                'Created user with username "Main bank" and password "123"'
            )
        )
