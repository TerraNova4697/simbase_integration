from pydantic_settings import BaseSettings
from pydantic import Field

from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    # DATABASE
    DB_USERNAME: str = Field(validation_alias='DB_USERNAME')
    DB_PASSWORD: str = Field(validation_alias='DB_PASSWORD')
    DB_ADDRESS: str = Field(validation_alias='DB_ADDRESS')
    DB_NAME: str = Field(validation_alias='DB_NAME')
    DB_PORT: str = Field(validation_alias='DB_PORT')

    # LOGGER
    LOGGER: str = Field(validation_alias='LOGGER')
    LOG_LEVEL: str = Field(validation_alias='LOG_LEVEL')

    # MQTT Client
    MQTT_URL: str = Field(validation_alias='MQTT_URL')
    MQTT_PORT: int = Field(validation_alias='MQTT_PORT')
    GATEWAY_TOKEN: str = Field(validation_alias='GATEWAY_TOKEN')

    ENVIRONMENT: str = Field(validation_alias='ENVIRONMENT')

    @property
    def database_url(self):
        return f"mysql+pymysql://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_ADDRESS}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def is_prod(self):
        return self.ENVIRONMENT == 'PROD'

settings = Settings()
