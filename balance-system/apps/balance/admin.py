from apps.balance.models import Balance, Transaction
from django.contrib import admin


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass
