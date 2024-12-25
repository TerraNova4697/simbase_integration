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
        while True:
            logger.info("Initialize tasks")
            tasks_table = [
                self.fetch_from_example_table1,
                self.fetch_from_example_table2
            ]
            tasks = [asyncio.create_task(task()) for task in tasks_table]

            done_tasks, pending_tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)

            for task in done_tasks:
                if exc := task.exception():
                    logger.error(f"Task {task} raised an exception: {exc}")

            for task in pending_tasks:
                try:
                    task.cancel()
                    await task
                except asyncio.CancelledError:
                    logger.info(f"Task {task} successfully cancelled")
                except Exception as exc:
                    logger.exception(f"Task {task} raised an exception: {exc}")

            await asyncio.sleep(10)


    async def fetch_from_example_table1(self):
        # Бизнес логика для получения данных из таблицы 1
        # Пример таска
        # Ex:
        # result = GpsORM.get_all_data_within_period(
        #     datetime.now(), datetime.now() - timedelta(minutes=1)
        # )
        # ...
        while True:
            await asyncio.sleep(4)
            logger.info("Some task1")

    async def fetch_from_example_table2(self):
        # Бизнес логика для получения данных из таблицы 2\
        while True:
            await asyncio.sleep(15)
            logger.info("Some task2")
