import asyncio
from datetime import datetime, timedelta, date

from tb_gateway_mqtt import TBGatewayMqttClient

from config.settings import settings
from connectors import Connector, Scheduler, TaskRunner
from database.queries.gps_orm import GpsORM
from destination.mqtt_client import CubaMqttClient
from logger import logger

from mock import mock

async def main():
    # Создаем клиента, который будет отправлять данные на платформу. Клиент работает на основе TBGatewayMqttClient
    mqtt_client = TBGatewayMqttClient(
        settings.MQTT_URL,
        int(settings.MQTT_PORT),
        settings.GATEWAY_TOKEN
    )
    # mqtt_client.connect()
    cuba_mqtt_client = CubaMqttClient(mqtt_client)

    # Коннектор, который будет собирать данные из конкретной БД и отправлять на платформу
    # Таких коннекторов может быть сколько угодно.
    scheduler = Scheduler(hour=6)
    task_runner = TaskRunner()
    
    connector = Connector(
        cuba_mqtt_client, scheduler=scheduler, task_runner=task_runner
    )

    # Запуск корутин всех коннекторов
    await asyncio.gather(
        connector.run_monitoring()
    )


if __name__ == '__main__':
    # from database.queries import FilialOrm, CustomerOrm, ObjectOrm

    # filials = ObjectOrm.get_all()
    # for f in filials:
    #     print(f)

    # mock()
    # from database.queries.filial_orm import FilialOrm
    # res = FilialOrm.get_all_filials()
    try:
        asyncio.run(main())
    finally:
        end_ts = datetime.timestamp(datetime.now())
