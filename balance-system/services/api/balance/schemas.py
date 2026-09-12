import pydantic

from apps.balance.choices import Currency
from services.api.common.schemas import CamelCaseSchema


class BalanceResponseSchema(CamelCaseSchema):
    owner_id: int
    amount: int = pydantic.Field(gt=0)
    currency: Currency = Currency.USD


class BalanceRequestSchema(CamelCaseSchema):
    amount: int = pydantic.Field(gt=0)
    currency: Currency = Currency.USD
