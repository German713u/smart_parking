# src/smart_parking/domain/money.py
from typing import Annotated

from pydantic import BaseModel, Field, field_validator


class Money(BaseModel):
    amount: Annotated[int, Field(ge=0)]
    currency: Annotated[str, Field(min_length=3, max_length=3)] = "USD"

    model_config = dict(frozen=True)

    @field_validator("currency")
    @classmethod
    def to_upper_iso(cls, v: str) -> str:
        v = v.upper()
        if not v.isalpha():
            raise ValueError("currency must be alphabetic code")
        return v

    def __add__(self, other: "Money") -> "Money":
        self._check_currency(other)
        return Money(amount=self.amount + other.amount, currency=self.currency)

    def __mul__(self, factor: float) -> "Money":
        return Money(amount=int(self.amount * factor), currency=self.currency)

    def _check_currency(self, other: "Money"):
        if self.currency != other.currency:
            raise ValueError("currency mismatch")
