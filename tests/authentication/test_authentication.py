from http import HTTPStatus
import pytest
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


""" 
Основная цель теста — проверка успешной аутентификации
 = создание пользователя — не часть самого теста. 
 ВЫНОСИМ В ФИКСТУРУ Создание Пользователя"""
@pytest.mark.regression
@pytest.mark.authentication
class TestAuthentication:

    def test_login(self,
            function_user: UserFixture,  # Используем фикстуру для создания пользователя
            authentication_client: AuthenticationClient
    ):
        # В ФИКСТУРАХ API-клиент для работы с пользователями. Public_users_client - Подтягивается из function_user
        # function_user - СОЗДАЕТ ПОЛЬЗОВАТЕЛЯ.

        # Запрос на логин (login_request -> request)
        # Достаем email password из Запроса на создание пользователя
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        # Выполняем логин (login_response -> response)
        response = authentication_client.login_api(request)
        # Валидация ответа (login_response_data -> response_data)
        # Десериализация Ответа в Pydantic Модель + валидация
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        # проверка Токенов (type = bearer + не пустые)
        assert_login_response(response_data)

        # login_response.json() = Настоящий ответ. Строго валидирует Типы данных, без их преобразования.
        # jsonSchema. Сервер вернул данные нужных типов
        validate_json_schema(response.json(), response_data.model_json_schema())









