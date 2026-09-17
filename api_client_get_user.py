"""
Создаст пользователя через API.
Авторизуется под этим пользователем.
Получит его данные по эндпоинту /api/v1/users/{user_id}.
"""

from clients.private_http_builder import AuthenticationUserDict
from clients.users.private_user_client import get_private_users_client
from clients.users.public_users_client import get_public_client, CreateUserRequestDict
from tools.fakers import get_random_email

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_client()

# Инициализируем ТЕЛО ЗАПРОСА на создание пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
# Отправляем POST запрос на создание пользователя
# через метод create_user, который сразу возвращает JSON ответ
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
# Инициализируем клиент PrivateUsersClient
# Который сразу настроен с Заголовками аутентификации
private_users_client = get_private_users_client(authentication_user)

# Отправляем GET запрос на получение данных пользователя
# Через метод get_user, который сразу возвращает JSON ответ
get_user_response = private_users_client.get_user(create_user_response['user']['id'])
print('Get user data:', get_user_response)




