import tomllib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

CONFIG_FILE = BASE_DIR / "config.toml"

if not CONFIG_FILE.exists():
    CONFIG_FILE = BASE_DIR / "default_config.toml"

with CONFIG_FILE.open("rb") as config_file:
    config = tomllib.load(config_file)

SECRET_KEY = config["base"]["secret_key"]
DEBUG = config["base"]["debug"]
ALLOWED_HOSTS = config["base"]["allowed_hosts"]

ROOT_URLCONF = "config.urls"

AUTH_USER_MODEL = "users.User"

WSGI_APPLICATION = "config.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
