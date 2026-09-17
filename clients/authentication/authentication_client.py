from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


# позволяет создавать строгие типизированные словари,
# указывая обязательные поля
class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


class RefreshRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления токена.
    """
    refreshToken: str  # Название ключа совпадает с API


class Token(TypedDict):
    """
    Описание структуры ЗАПРОСА на аутентификацию.
    """
    tokenType: str
    accessToken: str
    refreshToken: str


class LoginResponseDict(TypedDict):
    """
    Описание структуры ОТВЕТА аутентификации.
    """
    token: Token




class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request)


    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)




    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        """
        Отправляет запрос аутентификации на сервер.
        Возвращает JSON-ОТВЕТ
        """
        response = self.login_api(request)  # Отправляем запрос на аутентификацию
        return response.json()  # Извлекаем JSON из ответа





def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())

# Импортируем get_public_http_client() и используем его для создания HTTP-клиента.
# Передаем этот клиент в AuthenticationClient.
# Теперь, вызывая get_authentication_client(), мы получаем полностью готовый к использованию API-клиент.

# Код становится чище: при инициализации тестов не нужно вручную создавать httpx.Client.
# Гибкость: если в будущем потребуется изменить таймаут, заголовки или другие настройки,
# это можно сделать в одном месте (в get_public_http_client()), и изменения автоматически применятся ко всем API-клиентам.