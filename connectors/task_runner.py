import asyncio
from logger import logger

from database.queries import *
from util_functions import try_times
from destination.mqtt_client import CubaMqttClient
from destination.superset import Superset


class TaskRunner:

    def __init__(self, superset: Superset, mqtt_client: CubaMqttClient):
        self.superset: Superset = superset
        self.mqtt_client: CubaMqttClient = mqtt_client
        self.tasks_table = [
            self.fetch_filials,
            self.fetch_customers,
            self.fetch_objects,
            self.fetch_mobile_groups,
            self.fetch_posts,
            self.fetch_security_guards,
            self.fetch_income,
            # self.fetch_route_sheet,
        ]

    async def run_tasks(self):
        tasks = [asyncio.create_task(task()) for task in self.tasks_table]

        done_tasks, pending_tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)

        for task in done_tasks:
            if exc := task.exception():
                logger.error(f"{task=} raised an exception: {exc}")

        for task in pending_tasks:
            try:
                task.cancel()
                await task
            except asyncio.CancelledError:
                logger.info(f"{task=} successfully cancelled")
            except Exception as exc:
                logger.exception(f"{task=} raised an exception: {exc}")

    @try_times(number_of_tries=3)
    async def fetch_filials(self):
        simbase_filials = FilialOrm.all()
        self.superset.consume_filials(simbase_filials)
        logger.info("Fetched filials")

    @try_times(number_of_tries=3)
    async def fetch_customers(self):
        simbase_customers = CustomerOrm.all()
        self.superset.consume_customers(simbase_customers)
        logger.info("Fetched customers")

    @try_times(number_of_tries=3)
    async def fetch_objects(self):
        simbase_objects = ObjectOrm.all()
        self.superset.consume_objects(simbase_objects)
        logger.info("Fetched objects")

    @try_times(number_of_tries=3)
    async def fetch_posts(self):
        simbase_posts = PostOrm.all()
        self.superset.consume_posts(simbase_posts)
        logger.info("Fetched posts")

    @try_times(number_of_tries=3)
    async def fetch_mobile_groups(self):
        simbase_mobile_groups = MobileGroupOrm.all()
        self.superset.consume_mobile_groups(simbase_mobile_groups)
        logger.info("Fetched mobile groups")

    @try_times(number_of_tries=3)
    async def fetch_route_sheet(self):
        simbase_route_sheet = RouteSheetOrm.all()
        self.superset.consume_route_sheet(simbase_route_sheet)
        logger.info("Fetched route sheet")

    @try_times(number_of_tries=3)
    async def fetch_security_guards(self):
        simbase_security_guards = SecurityGuardOrm.all()
        self.superset.consume_security_guards(simbase_security_guards)
        logger.info("Fetched security guards")

    @try_times(number_of_tries=3)
    async def fetch_income(self):
        simbase_income = IncomeOrm.all()
        self.superset.consume_income(simbase_income)
        logger.info("Fetched income")
