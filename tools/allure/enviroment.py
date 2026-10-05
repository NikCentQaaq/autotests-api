import platform
import sys

from config import settings


def create_allure_environment_file():
    # Создаем список из элементов в формате {key}={value}
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    # Собираем все элементы в единую строку с переносами
    items.append(f'os_info={platform.system()}, {platform.release()}')
    items.append(f'python_version={sys.version}')

    properties = '\n'.join(items)

    # Открываем файл ./allure-results/environment.properties
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)  # Записываем переменные в файл
