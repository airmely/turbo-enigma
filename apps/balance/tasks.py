import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def process_balance_task():
    try:
        process_balance_task_inner()
    except Exception as e:
        logger.error(e)


def process_balance_task_inner():
    pass
