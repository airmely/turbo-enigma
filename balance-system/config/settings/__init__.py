from split_settings.tools import include, optional

include(
    "base.py",
    "apps.py",
    "middleware.py",
    "templates.py",
    "database.py",
    "auth.py",
    "i18n.py",
    "static.py",
    "celery.py",
    "cache.py",
    optional("local_settings.py"),
)
