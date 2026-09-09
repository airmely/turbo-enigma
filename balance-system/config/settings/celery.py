import os

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/1")

CELERY_ACCEPT_CONTENT = ["json"]
CELERY_RESULT_BACKEND = os.environ.get(
    "CELERY_RESULT_BACKEND",
    "redis://localhost:6379/1",
)
CELERY_TASK_SERIALIZER = "json"
