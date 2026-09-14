import logging

from celery import shared_task
from django.contrib.auth import get_user_model

from apps.balance.exceptions import InsufficientFundsException, SelfTransferException
from apps.balance.services import TransactionService

logger = logging.getLogger(__name__)
ResultTransaction = dict[str, str]
User = get_user_model()


@shared_task
def process_transaction_task(
    sender_id: int,
    receiver_id: int,
    amount: int,
) -> ResultTransaction:
    """Background task"""
    try:
        # Implemented specifically through an additional function
        # so that unhandled exceptions can be caught
        process_transaction_task_inner(sender_id, receiver_id, amount)
    except (InsufficientFundsException, SelfTransferException) as e:
        return {"detail": str(e)}
    except User.DoesNotExist:
        logger.error(
            "User not found: sender_id=%s, receiver_id=%s",
            sender_id,
            receiver_id,
        )
        return {"detail": "User not found."}
    except Exception as e:
        logger.error(e)
        return {"detail": str(e)}
    logger.info(
        "Transaction processed successfully: sender_id=%s, receiver_id=%s, amount=%s",
        sender_id,
        receiver_id,
        amount,
    )
    return {"detail": "Transaction has been processed."}


def process_transaction_task_inner(
    sender_id: int,
    receiver_id: int,
    amount: int,
) -> None:
    sender = User.objects.select_related("balance").get(id=sender_id)
    receiver = User.objects.select_related("balance").get(id=receiver_id)
    transaction_service = TransactionService(
        sender=sender,
        receiver=receiver,
        amount=amount,
    )
    transaction_service.create_transaction()
    transaction_service.act()
