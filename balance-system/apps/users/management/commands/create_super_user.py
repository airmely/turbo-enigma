from django.core.management.base import BaseCommand

from apps.users.models import User


class Command(BaseCommand):
    help = "Create super user"

    def handle(self, *args, **options):

        if User.objects.filter(username="admin").exists():
            self.stdout.write(self.style.NOTICE("admin already exists"))
            return

        user = User.objects.create(
            username="admin",
            email="admin@admin.com",
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )

        user.set_password("1234")
        user.save()

        self.stdout.write(
            self.style.SUCCESS('Created user with username "admin" and password "1234"')
        )
