"""This module is FOR DEVELOPMENT ONLY!!! DO NOT USE it in production!!!"""

import random
from datetime import datetime, timedelta

from requests import session
from sqlalchemy import delete

from database.simbase_database import Base, engine, session_factory
from database.models import DeviceTelemetry
from config.settings import settings


device_ids = [
    '0061001',
    '0061002',
    '0061003',
    '0061004',
    '0061005',
    '0062001',
    '0062002',
    '0062003',
    '0062004',
    '0063001',
    '0063002',
    '0063003',
    '0063004',
    '0063005',
    '0063006',
    '0063007',
    '0063008',
]


class DataBaseOpsORM:
    """This class is FOR DEVELOPMENT ONLY!!! DO NOT USE it in production!!!"""

    @staticmethod
    def create_tables():
        """This method is FOR DEVELOPMENT ONLY!!! DO NOT USE it in production!!!"""
        if settings.is_prod:
            raise Exception('You are not allowed to run this function in production')
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    @staticmethod
    def delete_all_gps_records():
        """This method is FOR DEVELOPMENT ONLY!!! DO NOT USE it in production!!!"""
        if settings.is_prod:
            raise Exception('You are not allowed to run this function in production')
        with session_factory() as session:
            query = delete(DeviceTelemetry).where(True)
            print(query)
            session.execute(query)
            session.commit()

    @staticmethod
    def insert_fake_data():
        """This method is FOR DEVELOPMENT ONLY!!! DO NOT USE it in production!!!"""
        if settings.is_prod:
            raise Exception('You are not allowed to run this function in production')
        with session_factory() as session:
            start_time = datetime.now()
            end_time = datetime.now() + timedelta(hours=1)
            for device_id in device_ids:
                current_time = start_time
                rand_int = random.randrange(1, 100)
                while current_time <= end_time:
                    obj = DeviceTelemetry(
                        device_id=device_id,
                        device_alias=f'QWERTY{rand_int}',
                        device_type=1,
                        gps_datetime=current_time,
                        long_we='w',
                        longitude=51.1245235,
                        lat_ns='n',
                        latitude=71.2340,
                        speed=14.56,
                        direction=81.6664,
                        receive_datetime=current_time,
                        tsc_id=5,
                        rssi_up=5,
                        rssi_down=5,
                        power_mode=5,
                        electricity=100
                    )
                    session.add(obj)
                    current_time += timedelta(seconds=20)
            session.commit()
