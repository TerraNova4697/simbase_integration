import asyncio
from datetime import datetime, timedelta


class Scheduler:

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.hour: int = hour
        self.minute: int = minute
        self.second: int = second

    async def wait_till_next_iteration(self):
        # Calculate time for next iteration
        time_now = datetime.now()
        next_iteration_time = (time_now + timedelta(days=1)).replace(hour=self.hour, minute=self.minute, second=self.second)

        # Calculate seconds of sleep & sleep
        time_to_wait = next_iteration_time - time_now
        await asyncio.sleep(time_to_wait.seconds)
