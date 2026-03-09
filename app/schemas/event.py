from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

class EventType(Enum):
    port_scan = "port_scan"
    brute_force = "brute_force"
    ddos_spike = "ddos_spike"
    suspicious_payload = "suspicious_payload"
    authentication_failure = "authentication_failure"
    malware_like = "malware_like"

class EventCreate(BaseModel):
    timestamp: Optional[datetime] = None
    source_ip: str = Field(..., min_length=7, max_length=45)
    target: str
    port: int
    event_type: EventType
    payload: str
    ingestion_source: str

class EventRead(EventCreate):
    id: int = Field(..., example=1)

    class Config:
        orm_mode = True