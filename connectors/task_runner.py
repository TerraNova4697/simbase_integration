import asyncio
from logger import logger


class TaskRunner:

    def __init__(self):
        self.tasks_table = [
            self.fetch_from_example_table1,
            self.fetch_from_example_table2
        ]

    async def run_tasks(self):
        tasks = [asyncio.create_task(task()) for task in self.tasks_table]

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

    async def fetch_from_example_table1(self):
        # Бизнес логика для получения данных из таблицы 1
        # Пример таска
        # Ex:
        # result = GpsORM.get_all_data_within_period(
        #     datetime.now(), datetime.now() - timedelta(minutes=1)
        # )
        # ...
        await asyncio.sleep(4)
        logger.info("Some task1")

    async def fetch_from_example_table2(self):
        # Бизнес логика для получения данных из таблицы 2\
        await asyncio.sleep(15)
        logger.info("Some task2")
