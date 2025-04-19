from __future__ import annotations

import uuid
from dataclasses import field
from datetime import datetime, timezone
from enum import Enum

from pydantic.dataclasses import dataclass

from .license_plate import LicensePlate
from .money import Money


class SessionStatus(str, Enum):
    STARTED = "started"
    COMPLETED = "completed"


@dataclass(frozen=True, config=dict(validate_assignment=False))
class ParkingSession:
    id: str
    plate: LicensePlate
    started_at: datetime
    rate: float
    status: SessionStatus = SessionStatus.STARTED
    total: Money | None = None
    _events: list[object] = field(default_factory=list)

    def __post_init__(self):
        object.__setattr__(self, "_events", [])

    # ---------- fábricas --------------------------------------------------
    @classmethod
    def start(cls, plate: LicensePlate, rate: float) -> "ParkingSession":
        session = cls(
            id=str(uuid.uuid4()),
            plate=plate,
            started_at=datetime.now(timezone.utc),
            rate=rate,
        )
        session._record("SessionStarted")
        return session

    # ---------- comportamiento -------------------------------------------
    def complete(self, price: Money) -> "ParkingSession":
        if self.status == SessionStatus.COMPLETED:
            raise ValueError("session already completed")
        object.__setattr__(self, "total", price)
        object.__setattr__(self, "status", SessionStatus.COMPLETED)
        self._record("SessionCompleted")
        return self

    # ---------- eventos internos -----------------------------------------
    def _record(self, name: str) -> None:
        self._events.append({"name": name, "session_id": self.id})
