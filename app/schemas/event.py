from datetime import datetime
from enum import StrEnum
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, IPvAnyAddress


class EventType(StrEnum):
    port_scan = "port_scan"
    brute_force = "brute_force"
    ddos_spike = "ddos_spike"
    suspicious_payload = "suspicious_payload"
    authentication_failure = "authentication_failure"
    malware_like = "malware_like"

class EventCreate(BaseModel):
    timestamp: Optional[datetime] = None
    source_ip: IPvAnyAddress
    target: str
    port: int = Field(..., ge=1, le=65535)
    event_type: EventType = Field(...)
    payload: str
    ingestion_source: str

class EventRead(EventCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(...)
