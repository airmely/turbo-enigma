import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "whereDidYouForgetYourPassword?")

DEBUG = os.environ.get("DEBUG", "True") == "True"

ALLOWED_HOSTS: list[str] = []

ROOT_URLCONF = "config.urls"

AUTH_USER_MODEL = "users.User"

WSGI_APPLICATION = "config.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
