from pydantic import BaseModel, HttpUrl, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict



# данные настройки для http-client
class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    # свойство конвертации тип url в str, которую можно использовать
    @property
    def client_url(self) -> str:
        return str(self.url)

# тестовые данные (путь к файлам)
class TestDataConfig(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",  # Указываем, из какого файла читать настройки
        env_file_encoding="utf-8",  # Указываем кодировку файла
        env_nested_delimiter=".",  # Указываем разделитель для вложенных переменных
    )

    test_data: TestDataConfig
    http_client: HTTPClientConfig


# Инициализируем настройки
settings = Settings()




"""
Универсальный (через CONFIG_FILE)
Если хочется больше гибкости, можно вместо ENV передавать путь к файлу:

import os
from pydantic_settings import BaseSettings, SettingsConfigDict

config_file = os.getenv("CONFIG_FILE", ".env.local")


class Settings(BaseSettings):
    base_url: str
    db_dsn: str

    model_config = SettingsConfigDict(env_file=config_file)

                  
Теперь можно указать любой путь и даже другой формат (JSON, YAML):

CONFIG_FILE=configs/test.yaml pytest
CONFIG_FILE=.env.stage pytest

                  
Pydantic умеет работать не только с .env, но и с JSON/YAML, поэтому это расширяет возможности.

"""