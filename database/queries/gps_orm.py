from datetime import datetime

from sqlalchemy import select, and_, or_

from database.database import session_factory
from database.models import DeviceTelemetry


class GpsORM:

    @staticmethod
    def get_all_data_within_period(start_time: datetime, end_time: datetime):
        with session_factory() as session:
            query = (
                select(DeviceTelemetry)
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
            return session.execute(query).scalars().all()
