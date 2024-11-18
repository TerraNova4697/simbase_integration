import asyncio
from datetime import datetime, timedelta
import logging

from config.settings import settings
from database.queries.gps_orm import GpsORM
from destination.mqtt_client import CubaMqttClient


logger = logging.getLogger(settings.LOGGER)


class HyteraConnector:

    def __init__(self, destination):
        self.gps_orm: GpsORM
        self.destination: CubaMqttClient = destination

    async def run_monitoring(self):
        await self.get_radiostations_state(seconds=60)

    async def get_radiostations_state(self, minutes: int = 0, seconds: int = 0):
        start = datetime.now() - timedelta(minutes=minutes, seconds=seconds)
        while True:
            end = datetime.now()
            logger.info(f"Start loop at {start} end at {end}")
            telemetry = await self.form_telemetry_grouped_by_name(start, end)
            for device_name, telemetry_pack in telemetry.items():
                self.destination.send_data_pack(device_name, telemetry_pack)
            start = end
            next_iteration = start + timedelta(minutes=minutes, seconds=seconds)
            wait_time = (next_iteration - datetime.now()).seconds
            logger.info(type(wait_time))
            if wait_time > 0:
                logger.info(f"End loop. Wait {wait_time} seconds")
                logger.info('--------------------------------')
                await asyncio.sleep(wait_time)

    @staticmethod
    async def form_telemetry_grouped_by_name(start: datetime, end: datetime) -> dict[list]:
        all_data = GpsORM.get_all_data_within_period(start, end)
        formed_telemetry = {}
        for record in all_data:
            obj = {
                "ts": int(datetime.timestamp(record.gps_datetime) * 1000),
                "values": {
                    "long_we": record.long_we,
                    "longitude": float(record.longitude),
                    "lat_ns": record.lat_ns,
                    "latitude": float(record.latitude),
                    "speed": float(record.speed),
                    "direction": float(record.direction),
                    "receive_datetime": int(datetime.timestamp(record.receive_datetime) * 1000),
                    "rssi_up": record.rssi_up,
                    "rssi_down": record.rssi_down,
                    "power_mode": record.power_mode,
                    "electricity": record.electricity
                }
            }
            if not formed_telemetry.get(record.device_id):
                formed_telemetry[record.device_id] = [obj]
            else:
                formed_telemetry[record.device_id].append(obj)

        return formed_telemetry
