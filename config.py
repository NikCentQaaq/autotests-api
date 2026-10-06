from typing import Self

from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath
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
        extra='allow',  # Разрешаем дополнительные переменные (для CI-CD)
        env_file=".env",  # Указываем, из какого файла читать настройки
        env_file_encoding="utf-8",  # Указываем кодировку файла
        env_nested_delimiter=".",  # Указываем разделитель для вложенных переменных
    )

    test_data: TestDataConfig
    http_client: HTTPClientConfig
    allure_results_dir: DirectoryPath


    # Создает директорию allure-results, если она не существует
    # Инициализирует модель с параметром allure_results_dir
    @classmethod
    def initialize(cls) -> Self:  # Возвращает экземпляр класса Settings
        allure_results_dir = DirectoryPath("./allure-results")  # Создаем объект пути к папке
        allure_results_dir.mkdir(exist_ok=True)
        # Создаем папку allure-results, если она не существует

        # Передаем allure_results_dir в инициализацию настроек
        return Settings(allure_results_dir=allure_results_dir)


# Инициализируем настройки
settings = Settings.initialize()




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