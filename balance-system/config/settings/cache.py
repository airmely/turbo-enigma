import os

REDIS_CELERY_URL = os.environ.get("REDIS_CELERY_URL", "redis://localhost:6379/1")

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": REDIS_CELERY_URL,
    }
}
