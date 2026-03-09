from datetime import datetime
import pytest
from pydantic import ValidationError
from sqlalchemy import event

from app.schemas.event import EventCreate, EventRead, EventType


def valid_event_data():
    return {
        "timestamp": "2026-03-09T10:30:00",
        "source_ip": "192.168.1.10",
        "target": "server-1",
        "port": 443,
        "event_type": "port_scan",
        "payload": "GET /admin",
        "ingestion_source": "sensor-01",
    }


def test_event_create_valid():
    data = valid_event_data()
    event = EventCreate(**data)

    assert str(event.source_ip) == "192.168.1.10"
    assert event.port == 443
    assert event.event_type == EventType.port_scan
    assert event.ingestion_source == "sensor-01"
    assert isinstance(event.timestamp, datetime)


def test_event_create_timestamp_can_be_none():
    data = valid_event_data()
    data["timestamp"] = None

    event = EventCreate(**data)

    assert event.timestamp is None


def test_event_create_invalid_port_too_small():
    data = valid_event_data()
    data["port"] = 0

    with pytest.raises(ValidationError) as exc_info:
        EventCreate(**data)

    assert "port" in str(exc_info.value)


def test_event_create_invalid_port_too_large():
    data = valid_event_data()
    data["port"] = 70000

    with pytest.raises(ValidationError) as exc_info:
        EventCreate(**data)

    assert "port" in str(exc_info.value)


def test_event_create_invalid_source_ip_too_short():
    data = valid_event_data()
    data["source_ip"] = "1.1"

    with pytest.raises(ValidationError) as exc_info:
        EventCreate(**data)

    assert "source_ip" in str(exc_info.value)


def test_event_create_invalid_event_type():
    data = valid_event_data()
    data["event_type"] = "some_weird_attack"

    with pytest.raises(ValidationError) as exc_info:
        EventCreate(**data)

    assert "event_type" in str(exc_info.value)


def test_event_create_missing_required_field():
    data = valid_event_data()
    del data["payload"]

    with pytest.raises(ValidationError) as exc_info:
        EventCreate(**data)

    assert "payload" in str(exc_info.value)


def test_event_read_valid():
    data = valid_event_data()
    data["id"] = 1

    event = EventRead(**data)

    assert event.id == 1
    assert event.event_type == EventType.port_scan


class DummyEvent:
    def __init__(self):
        self.id = 99
        self.timestamp = datetime(2026, 3, 9, 10, 30, 0)
        self.source_ip = "10.0.0.5"
        self.target = "auth-service"
        self.port = 22
        self.event_type = EventType.brute_force
        self.payload = "failed login attempts"
        self.ingestion_source = "honeypot"


def test_event_read_from_attributes():
    obj = DummyEvent()

    event = EventRead.model_validate(obj)

    assert event.id == 99
    assert str(event.source_ip) == "10.0.0.5"
    assert event.event_type == EventType.brute_force