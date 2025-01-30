import asyncio

from tb_gateway_mqtt import TBGatewayMqttClient

from config.settings import settings
from connectors import Connector, Scheduler, TaskRunner
from database.queries.gps_orm import GpsORM
from destination.mqtt_client import CubaMqttClient
from destination.superset import Superset
from logger import logger


async def main():
    # Создаем клиента, который будет отправлять данные на платформу. Клиент работает на основе TBGatewayMqttClient
    mqtt_client = TBGatewayMqttClient(
        settings.MQTT_URL,
        int(settings.MQTT_PORT),
        settings.GATEWAY_TOKEN
    )
    # mqtt_client.connect()
    cuba_mqtt_client = CubaMqttClient(mqtt_client)
    superset = Superset()

    # Коннектор, который будет собирать данные из конкретной БД и отправлять на платформу
    # Таких коннекторов может быть сколько угодно.
    scheduler = Scheduler(hour=6)
    task_runner = TaskRunner(mqtt_client=mqtt_client, superset=superset)
    
    connector = Connector(
        scheduler=scheduler, task_runner=task_runner
    )

    # Запуск корутин всех коннекторов
    await asyncio.gather(
        connector.run_monitoring()
    )


if __name__ == '__main__':
    try:
        asyncio.run(main())
    finally:
        logger.info("Shutting down.")
