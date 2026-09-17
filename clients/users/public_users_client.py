from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


# PublicUsersClient – для публичных методов,
# не требующих авторизации.

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class User(TypedDict):
    """
    Описание структуры пользователя.
    То, что будет внутри 'user'
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ОТВЕТА создания пользователя.
    """
    user: User


class PublicUsersClient(APIClient):
    """
    Клиент для работы с  /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email, password, lastName, firstName, middleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)



    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        # Вызов метода Создания пользователя
        response = self.create_user_api(request)
        # Возвращает ТЕЛО ОТВЕТА
        return response.json()




def get_public_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())

