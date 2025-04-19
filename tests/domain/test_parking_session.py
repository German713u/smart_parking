import pytest

from smart_parking.domain.license_plate import LicensePlate
from smart_parking.domain.money import Money
from smart_parking.domain.parking_session import ParkingSession, SessionStatus


def test_license_plate_validation():
    with pytest.raises(ValueError):
        LicensePlate(value="12-AAA")


def test_session_lifecycle():
    plate = LicensePlate(value="ABC-123")
    session = ParkingSession.start(plate, rate=1.5)
    assert session.status is SessionStatus.STARTED

    session.complete(Money(amount=150))
    assert session.status is SessionStatus.COMPLETED
    assert session.total.amount == 150
