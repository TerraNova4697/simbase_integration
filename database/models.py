from datetime import datetime

from sqlalchemy import Integer, DateTime, Float, String, SmallInteger, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class DeviceTelemetry(Base):
    __tablename__ = 'gps_location_data_base'

    guid: Mapped[str] = mapped_column(String(length=64), primary_key=True)
    puc_id: Mapped[str] = mapped_column(String(length=64))
    system_id: Mapped[str] = mapped_column(String(length=16))
    device_id: Mapped[str] = mapped_column(String(length=64))
    device_alias: Mapped[str] = mapped_column(String(length=100))
    device_type: Mapped[int]
    staff_code: Mapped[str] = mapped_column(String(length=50))
    gps_datetime: Mapped[datetime]
    gps_av: Mapped[str] = mapped_column(String(length=1))
    long_we: Mapped[str] = mapped_column(String(length=1))
    longitude: Mapped[float] = mapped_column(Numeric(precision=20, scale=16))
    lat_ns: Mapped[str] = mapped_column(String(length=1))
    latitude: Mapped[float] = mapped_column(Numeric(precision=20, scale=16))
    speed: Mapped[float] = mapped_column(Numeric(precision=20, scale=16))
    direction: Mapped[float] = mapped_column(Numeric(precision=20, scale=16))
    state: Mapped[str] = mapped_column(String(255))
    receive_datetime: Mapped[datetime]
    tsc_id: Mapped[int]
    channel_id: Mapped[int] = mapped_column(SmallInteger)
    rssi_up: Mapped[int] = mapped_column(SmallInteger)
    rssi_down: Mapped[int] = mapped_column(SmallInteger)
    power_mode: Mapped[int] = mapped_column(SmallInteger)
    electricity: Mapped[int]
