from httpx import Client

# публичный клиент = НЕ нуждается в каких-то заголовках


# инициализирует готовый экземпляр класса httpx.Client
def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(timeout=100, base_url="http://127.0.0.1:8000")




