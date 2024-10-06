from apps.base.exceptions import BaseAppException


class BalanceException(BaseAppException):
    """Base class for balance-related exceptions."""

    pass


class InsufficientFundsException(BalanceException):
    """Raised when there are insufficient funds in the account."""


class SelfTransferException(BalanceException):
    """Raised when a user attempts to send money to themselves."""
