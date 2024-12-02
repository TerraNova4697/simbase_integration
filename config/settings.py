import logging
import os
from time import sleep

from dotenv import load_dotenv


load_dotenv()


class Settings:

    def __init__(self):
        self.DB_USERNAME = os.environ.get('DB_USERNAME')
        self.DB_PASSWORD = os.environ.get('DB_PASSWORD')
        self.DB_ADDRESS = os.environ.get('DB_ADDRESS')
        self.DB_NAME = os.environ.get('DB_NAME')
        self.DB_PORT = os.environ.get('DB_PORT')
        self.LOGGER = os.environ.get('LOGGER')
        self.MQTT_URL = os.environ.get('MQTT_URL')
        self.MQTT_PORT = os.environ.get('MQTT_PORT')
        self.GATEWAY_TOKEN = os.environ.get('GATEWAY_TOKEN')

        self.DEBUG = bool(int(os.environ.get('DEBUG')))
        self.TEST = bool(int(os.environ.get("TEST")))
        self.PROD = False if self.DEBUG else bool(int(os.environ.get('PROD')))
        self.logger = self.config_log()
        if not self.DEBUG and not self.TEST and self.PROD:
            self.ENVIRONMENT = 'PROD'
            self.logger.info("Running in production mode...")
        elif self.TEST:
            self.ENVIRONMENT = 'TEST'
            self.logger.info('Running in testing mode...')
        else:
            self.ENVIRONMENT = 'DEVELOPMENT'
            self.logger.info('Running in development mode...')
            self.logger.info("If you want to run in production, you must set TEST and DEBUG to '0'")

    @property
    def database_url(self):
        return f"postgresql://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_ADDRESS}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def is_development(self):
        return self.ENVIRONMENT == 'DEVELOPMENT'

    @property
    def is_testing(self):
        return self.ENVIRONMENT == 'TEST'

    @property
    def is_prod(self):
        return self.ENVIRONMENT == 'PROD'

    @property
    def mqtt_url(self):
        return self.MQTT_URL

    @property
    def mqtt_port(self):
        return self.MQTT_PORT

    @property
    def gateway_token(self):
        return self.GATEWAY_TOKEN

    def __repr__(self):
        return f"{self.DEBUG=} - {type(self.DEBUG)} | {self.PROD=} - {type(self.PROD)}"

    def config_log(self):
        logger = logging.getLogger(self.LOGGER)

        file_handler = logging.FileHandler(
            filename='logs/development.log', mode="a", encoding="utf-8"
        )
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(lineno)s - %(message)s"
            )
        )
        logger.addHandler(file_handler)
        if self.DEBUG:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
        return logger

settings = Settings()
