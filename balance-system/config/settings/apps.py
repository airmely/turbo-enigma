CONTRIB_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "apps.balance.apps.BalanceConfig",
    "apps.users.apps.UsersConfig",
]

THIRD_PARTY_APPS = [
    "dmr",
]

INSTALLED_APPS = CONTRIB_APPS + PROJECT_APPS + THIRD_PARTY_APPS
