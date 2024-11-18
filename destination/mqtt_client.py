import asyncio
import os
import logging

from tb_device_mqtt import TBPublishInfo
from tb_gateway_mqtt import TBGatewayMqttClient


logger = logging.getLogger(os.environ.get('LOGGER'))


class CubaMqttClient:

    def __init__(self, mqtt_client: TBGatewayMqttClient):
        self.mqtt_client: TBGatewayMqttClient = mqtt_client

    def send_data(self, device_name: str, telemetry: dict) -> bool:
        result = self.mqtt_client.gw_send_telemetry(device_name, telemetry)
        successful = result.rc() == TBPublishInfo.TB_ERR_SUCCESS
        if not successful:
            logger.warning(f"Telemetry was not sent: {device_name}, {telemetry}")
        return result.rc() == TBPublishInfo.TB_ERR_SUCCESS

    def send_data_pack(self, device_name: str, telemetry: list) -> bool:
        result = self.mqtt_client.gw_send_telemetry(device_name, telemetry)
        successful = result.rc() == TBPublishInfo.TB_ERR_SUCCESS
        if not successful:
            logger.warning(f"Telemetry was not sent: {device_name}, {telemetry}")
        return result.rc() == TBPublishInfo.TB_ERR_SUCCESS
