import pytest
from pydantic import BaseModel, EmailStr

from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_user_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema




# МОДЕЛЬ Pydantic для агрегации возвращаемых данных фикстурой function_user
class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema
    # доступ сразу и к запросу, и к ответу

    # декоратор, который позволяет вызывать метод как обычное поле (АТРИБУТ)
    # то есть Доступ по UserFixture.email
    @property
    def email(self) -> EmailStr:  # Быстрый доступ к email пользователя
        return self.request.email

    @property
    def password(self) -> str:  # Быстрый доступ к password пользователя
        return self.request.password

    # Из двух значений Модель Pydantic. Можно просто передать ее для авторизации
    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email, password=self.password)




@pytest.fixture  # по умолчанию скоуп function
def public_users_client() -> PublicUsersClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с публичным API пользователей
    return get_public_users_client()


# Публичный создает пользователя - передает данные через function_user
# с токенами создается Приватный
@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    return get_private_users_client(function_user.authentication_user)



# Фикстура СОЗДАЕТ ПОЛЬЗОВАТЕЛЯ
@pytest.fixture
# Используем фикстуру public_users_client, которая создает нужный API клиент
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    # Формируем тело запроса с рандомными данными
    request = CreateUserRequestSchema()
    # Вызываем запрос
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)
    # Возвращаем все нужные данные. Доступ и к запросу, и к ответу
# через Модель

