import asyncio
from datetime import datetime, timedelta, date
import logging

from config.settings import settings
from database.queries.gps_orm import GpsORM
from destination.mqtt_client import CubaMqttClient
from database.queries import FetchedDatesOrm
from .scheduler import Scheduler
from .task_runner import TaskRunner


logger = logging.getLogger(settings.LOGGER)


class Connector:

    def __init__(self, destination, scheduler: Scheduler, task_runner: TaskRunner):
        self.destination: CubaMqttClient = destination
        self.scheduler: Scheduler = scheduler
        self.task_runner: TaskRunner = task_runner

    async def run_monitoring(self):
        # Основная корутина коннектора. Отсюда в бекграунде запускаются таски коннектора
        while True:
            if self.record_exists_for_date(date.today()):
                logger.info("Record for today already fetched.")
                await self.scheduler.wait_till_next_iteration()
            
            logger.info("Initialize tasks")
            await self.task_runner.run_tasks()
            FetchedDatesOrm.create(date.today())
            await self.scheduler.wait_till_next_iteration()

    def record_exists_for_date(self, date):
        record = FetchedDatesOrm.get_last()
        if not record:
            return False
        return record.date_created == date
