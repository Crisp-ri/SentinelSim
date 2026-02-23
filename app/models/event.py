from app.db.base import Base
from sqlalchemy import  DateTime, Index, Integer, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class Event(Base):
    __tablename__ = "events"

    __table_args__ = (
        Index("ix_events_source_ip_timestamp", "source_ip", "timestamp"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    source_ip: Mapped[str] = mapped_column(String(45))
    target: Mapped[str] = mapped_column(String(255))
    port: Mapped[int] = mapped_column(Integer)
    event_type: Mapped[str] = mapped_column(String(255), index=True)
    payload: Mapped[str] = mapped_column(Text)
    ingestion_source: Mapped[str] = mapped_column(String(64))