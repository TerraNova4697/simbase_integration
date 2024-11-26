from datetime import datetime

from sqlalchemy import select, and_, or_

from database.database import session_factory_east, session_factory_west
from database.models import DeviceTelemetry


class GpsORM:

    @staticmethod
    def get_all_data_within_period_raw(start_time: datetime, end_time: datetime, source: str):
        if source == 'west':
            source_session = session_factory_west
        else:
            source_session = session_factory_east
        with source_session() as session:
            return session.execute(
                """
                SELECT 
                    device_id,
                    device_alias,
                    device_type,
                    gps_datetime,
                    longitude,
                    latitude,
                    speed,
                    direction,
                    receive_datetime,
                    rssi_up,
                    rssi_down,
                    power_mode,
                    electricity
                FROM 
                    gps_location_data_base
                WHERE 
                    receive_datetime BETWEEN '2024-11-14 08:49:00' AND '2024-11-14 08:49:30'
                    AND (
                        (device_id LIKE '0061%')
                        OR (device_id LIKE '0062%')
                    );
                """
            )

    @staticmethod
    def get_all_data_within_period(start_time: datetime, end_time: datetime, source: str):
        if source == 'west':
            source_session = session_factory_west
        else:
            source_session = session_factory_east
        with source_session() as session:
            query = (
                select(
                    DeviceTelemetry.device_id,
                    DeviceTelemetry.device_alias,
                    DeviceTelemetry.device_type,
                    DeviceTelemetry.gps_datetime,
                    DeviceTelemetry.longitude,
                    DeviceTelemetry.latitude,
                    DeviceTelemetry.speed,
                    DeviceTelemetry.direction,
                    DeviceTelemetry.receive_datetime,
                    DeviceTelemetry.rssi_up,
                    DeviceTelemetry.rssi_down,
                    DeviceTelemetry.power_mode,
                    DeviceTelemetry.electricity
                )
                .where(
                    and_(
                        and_(
                            DeviceTelemetry.receive_datetime > start_time,
                            DeviceTelemetry.receive_datetime <= end_time
                        ),
                        or_(
                            DeviceTelemetry.device_id.like('0061%'),
                            DeviceTelemetry.device_id.like('0062%')
                        )
                    )
                )
            )
            return session.execute(query).all()
