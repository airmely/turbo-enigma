from apps.balance.rest import views
from django.urls import path

urlpatterns = [
    path(
        "balance/",
        views.GetBalanceAPIView.as_view(),
        name="balance-get",
    ),
    path(
        "transactions/",
        views.TransactionHistoryAPIView.as_view(),
        name="transaction-history",
    ),
    path(
        "transactions/<int:receiver_id>/",
        views.SendAmountUserToUserAPIView.as_view(),
        name="transaction-send-amount",
    ),
]
