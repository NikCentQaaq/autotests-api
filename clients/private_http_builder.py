# Приватный клиент – используется для запросов, которые требуют авторизации
# (здесь необходимо устанавливать заголовки с токеном доступа)

from httpx import Client
from pydantic import BaseModel

from clients.authentication.authentication_client import get_authentication_client
# Импортируем модель LoginRequestSchema
from clients.authentication.authentication_schema import LoginRequestSchema
from functools import lru_cache  # Импортируем функцию для кеширования

from clients.event_hooks import curl_event_hook


class AuthenticationUserSchema(BaseModel, frozen=True):  # Добавили параметр frozen=True
    email: str
    password: str


@lru_cache(maxsize=None)  # Кешируем возвращаемое значение
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    authentication_client = get_authentication_client()

    # Используем модель LoginRequestSchema
    # Значения теперь извлекаем не по ключу, а через атрибуты
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        trust_env=False, # не использовать прокси, работать напрямую (игнорируя впн)
        headers={"Authorization": f"Bearer {login_response.token.access_token}"},
        event_hooks={"request": [curl_event_hook]}
    )
