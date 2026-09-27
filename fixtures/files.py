import pytest
from pydantic import BaseModel

from clients.files.files_client import get_files_client, FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from fixtures.users import UserFixture



# Объект содержащий запрос на загрузку файла + ответ после создания файла
class FileFixture(BaseModel):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema

# создание клиента для работы с загрузкой файлов
# В аргумент передается пользователь, полученный через фикстуру UserFixture (содержит всю инфу о пользователе)
#метод get_files_client создает клиент, уже настроенный для работы от имени данного пользователя
@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_files_client(function_user.authentication_user)


#
@pytest.fixture
def function_file(files_client: FilesClient) -> FileFixture:
    request = CreateFileRequestSchema(upload_file="./testdata/files/img.png")
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)
