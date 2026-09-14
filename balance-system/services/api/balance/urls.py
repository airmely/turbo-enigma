from dmr.routing import Router, path

from services.api.balance import views

router = Router(
    "balances/",
    [
        path(
            "",
            views.BalanceController.as_view(),
            name="get-balance",
        ),
    ],
    tags=["Balance"],
)
