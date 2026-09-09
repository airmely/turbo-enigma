import tomllib
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEFAULT_CONFIG_FILE = BASE_DIR / "default_config.toml"
LOCAL_CONFIG_FILE = BASE_DIR / "config.toml"


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = base.copy()
    for key, value in override.items():
        if (
            key in merged
            and isinstance(merged[key], dict)
            and isinstance(value, dict)
        ):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


with DEFAULT_CONFIG_FILE.open("rb") as config_file:
    config = tomllib.load(config_file)

if LOCAL_CONFIG_FILE.exists():
    with LOCAL_CONFIG_FILE.open("rb") as local_config_file:
        local_config = tomllib.load(local_config_file)
    config = _deep_merge(config, local_config)

SECRET_KEY = config["base"]["secret_key"]
DEBUG = config["base"]["debug"]
ALLOWED_HOSTS = config["base"]["allowed_hosts"]

ROOT_URLCONF = "config.urls"

AUTH_USER_MODEL = "users.User"

WSGI_APPLICATION = "config.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
