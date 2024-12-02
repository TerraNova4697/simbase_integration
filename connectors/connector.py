import asyncio
from datetime import datetime, timedelta
import logging

from config.settings import settings
from database.queries.gps_orm import GpsORM
from destination.mqtt_client import CubaMqttClient


logger = logging.getLogger(settings.LOGGER)


class Connector:

    def __init__(self, destination):
        self.destination: CubaMqttClient = destination

    async def run_monitoring(self):
        # Основная корутина коннектора. Отсюда в бекграунде запускаются таски коннектора
        asyncio.create_task(self.fetch_from_example_table1())
        asyncio.create_task(self.fetch_from_example_table2())

    async def fetch_from_example_table1(self):
        # Бизнес логика для получения данных из таблицы 1
        # Пример таска
        # Ex:
        # result = GpsORM.get_all_data_within_period(
        #     datetime.now(), datetime.now() - timedelta(minutes=1)
        # )
        # ...
        raise NotImplemented

    async def fetch_from_example_table2(self):
        # Бизнес логика для получения данных из таблицы 2
        raise NotImplemented
