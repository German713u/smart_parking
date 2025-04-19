import re

from pydantic import BaseModel, validator

_PLATE_RE = re.compile(r"^[A-Z]{3}-?\d{3}$")


class LicensePlate(BaseModel):
    value: str

    class Config:
        frozen = True  # inmutable

    @validator("value")
    def validate_format(cls, v: str) -> str:
        if not _PLATE_RE.fullmatch(v):
            raise ValueError(f"invalid license plate: {v}")
        return v
