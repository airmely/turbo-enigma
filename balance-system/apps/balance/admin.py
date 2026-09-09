from django.contrib import admin

from apps.balance.models import Balance, Transaction


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass
