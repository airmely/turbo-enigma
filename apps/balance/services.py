import logging
from dataclasses import dataclass
from typing import Callable

from apps.balance.exceptions import (
    BalanceException,
    InsufficientFundsException,
    SelfTransferException,
)
from apps.balance.models import Transaction
from apps.base.services import BaseService
from apps.users.models import User

logger = logging.getLogger(__name__)


@dataclass
class TransactionService(BaseService):
    sender: "User"
    receiver: "User"
    amount: int
    transaction: "Transaction" = None

    def act(self) -> None:
        """Validate and perform the money transfer."""
        self.validate()
        self.create_transaction()

        try:
            self.perform_transfer()
            self.complete_transaction()
        except BalanceException as e:
            logger.error("Transaction failed: %s", str(e))
            self.fail_transaction()

    def get_validators(self) -> list[Callable]:
        """Return a list of validation methods."""
        return [
            self.verify_balance,
            self.validate_not_self_transfer,
        ]

    def verify_balance(self):
        """Check if the sender has sufficient funds."""
        if self.sender.balance.amount < self.amount:
            logger.error("Insufficient funds for user %s", self.sender.pk)
            raise InsufficientFundsException()

    def validate_not_self_transfer(self):
        """Ensure the sender is not sending money to themselves."""
        if self.sender == self.receiver:
            logger.error("The user tried to send funds to himself %s", self.amount)
            raise SelfTransferException()

    def perform_transfer(self):
        """Transfer the amount from sender to receiver."""
        sender_balance = self.sender.balance
        receiver_balance = self.receiver.balance
        sender_balance.amount -= self.amount
        receiver_balance.amount += self.amount
        sender_balance.save()
        receiver_balance.save()
        logger.info(
            "Transferred %s from user %s to user %s",
            self.amount,
            self.sender.pk,
            self.receiver.pk,
        )

    def create_transaction(self):
        """Create a transaction record in the database."""
        self.transaction = Transaction.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            amount=self.amount,
            action=Transaction.WITHDRAW,
            status=Transaction.PENDING,
        )

    def complete_transaction(self):
        """Update the transaction status to complete."""
        if self.transaction:
            self.transaction.status = Transaction.COMPLETED
            self.transaction.save()
            logger.info("Transaction %s completed successfully.", self.transaction.pk)

    def fail_transaction(self):
        """Update the transaction status to failed."""
        if self.transaction:
            self.transaction.status = Transaction.FAILED
            self.transaction.save()
            logger.info("Transaction %s failed.", self.transaction.pk)
