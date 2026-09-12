CELERY_BROKER_URL = config["celery"]["broker_url"]

CELERY_ACCEPT_CONTENT = ["json"]
CELERY_RESULT_BACKEND = config["celery"]["result_backend"]
CELERY_TASK_SERIALIZER = "json"
