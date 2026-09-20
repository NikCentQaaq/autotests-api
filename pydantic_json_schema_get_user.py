from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_user_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake



# Получаем объект Клиента публичного - БЕЗ авторизации
public_users_client = get_public_users_client()
# ТЕЛО для запроса на создание user
create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
# Отправка запроса на Создание с Телом create_user_request
create_user_response = public_users_client.create_user(create_user_request)

# МОДЕЛЬ АВТОРИЗАЦИИ.
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# Приватный клиент - С ЗАГОЛОВКАМИ
private_users_client = get_private_users_client(authentication_user)

# Приватный клиент Запрос на получение инфы Пользователя по ID, который берем с ОТВЕТА СОЗДАНИЯ user
get_user_response = private_users_client.get_user_api(create_user_response.user.id) # передаем ID в query пармаетры
# Получаем Схему по МОДЕЛИ ОТВЕТА
get_user_response_schema = GetUserResponseSchema.model_json_schema()
# Валидируем ответ по схеме
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)

