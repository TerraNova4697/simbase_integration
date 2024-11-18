import asyncio
from datetime import datetime, timedelta

from tb_gateway_mqtt import TBGatewayMqttClient

from config.settings import settings
from connectors.hytera_connector import HyteraConnector
from database.queries.db_ops import DataBaseOpsORM
from destination.mqtt_client import CubaMqttClient


async def main():
    DataBaseOpsORM.insert_fake_data()
    mqtt_client = TBGatewayMqttClient(
        settings.mqtt_url,
        int(settings.MQTT_PORT),
        settings.gateway_token
    )
    mqtt_client.connect()
    cuba_mqtt_client = CubaMqttClient(mqtt_client)
    hytera_connector = HyteraConnector(cuba_mqtt_client)
    await hytera_connector.run_monitoring()


if __name__ == '__main__':
    settings.config_log()

    # DataBaseOpsORM.delete_all_gps_records()

    try:
        asyncio.run(main())
    finally:
        end_ts = datetime.timestamp(datetime.now())
