from http import HTTPStatus
import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.users.private_user_client import PrivateUsersClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tests.conftest import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response

@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient):
    # В ФИКСТУРЕ инициализируем API-клиент для работы с пользователями


    # Формируем тело запроса на создание пользователя
    request = CreateUserRequestSchema()
    # Отправляем запрос на создание пользователя
    response = public_users_client.create_user_api(request)
    # Инициализируем модель ответа на основе полученного JSON в ответе
    # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    # Проверяем статус-код ответа
    assert_status_code(response.status_code, HTTPStatus.OK)

    # Проверяем, что данные ответа совпадают с данными запроса
    # Используем функцию для проверки ответа создания юзера
    assert_create_user_response(request, response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())


def aassert_get_user_response(request, response_data):
    pass


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(
        function_user: UserFixture,
        private_users_client: PrivateUsersClient):
# function_user - СОЗДАЕТ ПОЛЬЗОВАТЕЛЯ.

    # Зарос GET
    # private_client настроен с токенами авторизации
    response = private_users_client.get_user_me_api()
    # Десериализация Ответа в Pydantic Модель + валидация
    response_data = GetUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)

    # function_user.response - достаем данные "ответ на создание"
    aassert_get_user_response(request=function_user.response, response_data=response_data)

    # login_response.json() = Настоящий ответ. Строго валидирует Типы данных, без их преобразования.
    # jsonSchema. Сервер вернул данные нужных типов
    validate_json_schema(response.json(), response_data.model_json_schema())



