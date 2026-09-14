from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.balance.exceptions import InsufficientFundsException, SelfTransferException
from apps.balance.models import Transaction
from apps.balance.tasks import process_transaction_task_inner

User = get_user_model()


class TransactionServiceTests(TestCase):

    def setUp(self):
        self.sender = User.objects.create(
            username="sender",
            email="test1@test.com",
            password="test1",
        )
        self.sender.balance.amount = 100
        self.sender.balance.save()
        self.receiver = User.objects.create(
            username="receiver",
            email="test2@test.com",
            password="test2",
        )
        self.receiver.balance.amount = 50
        self.receiver.balance.save()

    def test_successful_transaction(self):
        """Successful fund transfer test."""
        process_transaction_task_inner(
            self.sender.pk,
            self.receiver.pk,
            amount=50,
        )
        self.sender.refresh_from_db()
        self.receiver.refresh_from_db()
        self.assertEqual(self.sender.balance.amount, 50)
        self.assertEqual(self.receiver.balance.amount, 100)
        transaction = Transaction.objects.get(
            sender=self.sender,
            receiver=self.receiver,
        )
        self.assertEqual(transaction.status, Transaction.COMPLETED)

    def test_insufficient_funds(self):
        """Test of insufficient funds for the sender."""
        with self.assertRaises(InsufficientFundsException):
            process_transaction_task_inner(
                self.sender.pk,
                self.receiver.pk,
                amount=150,
            )

        self.sender.refresh_from_db()  # noqa
        self.receiver.refresh_from_db()
        self.assertEqual(self.sender.balance.amount, 100)
        self.assertEqual(Transaction.objects.count(), 1)
        transaction = Transaction.objects.get(
            sender=self.sender,
            receiver=self.receiver,
        )
        self.assertEqual(transaction.status, Transaction.FAILED)

    def test_self_transfer(self):
        """Test of an attempt to transfer funds to yourself."""
        with self.assertRaises(SelfTransferException):
            process_transaction_task_inner(
                self.sender.pk,
                self.sender.pk,
                amount=50,
            )
        self.sender.refresh_from_db()  # noqa
        self.receiver.refresh_from_db()
        self.assertEqual(self.sender.balance.amount, 100)
        self.assertEqual(Transaction.objects.count(), 1)
        transaction = Transaction.objects.get(
            sender=self.sender,
            receiver=self.sender,
        )
        self.assertEqual(transaction.status, Transaction.FAILED)
