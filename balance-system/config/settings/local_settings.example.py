# Copy to local_settings.py for local development overrides (gitignored).

INSTALLED_APPS += [
    "django_extensions",
    "debug_toolbar",
]

INTERNAL_IPS = ["127.0.0.1", "localhost"]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
