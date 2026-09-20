from typing import List

from pydantic import BaseModel, Field, EmailStr, ConfigDict


class AuthorSchema(BaseModel):
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    id: str
    email: EmailStr
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

class CourseSchema(BaseModel):
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    id: str
    title: str
    price: int
    author: AuthorSchema
    tags: List[str]



response_json = {
    "id": "course-123",
    "title": "Python API Automation",
    "price": 500,
    "author": {
        "id": "user-1",
        "email": "teacher@test.com",
        "firstName": "Alex",
        "lastName": "Smith"
    },
    "tags": [
        "python",
        "api",
        "testing"
    ]
}

course_model = CourseSchema(**response_json)

print(course_model.title)
print(course_model.author.email)
print(course_model.author.get_full_name())
print(course_model.tags[0])














from pydantic import BaseModel, ConfigDict


class AddressSchema(BaseModel):
    city: str
    zip_code: str


class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True  # Значение по умолчанию
    address: AddressSchema  # Вложенная модель

user = UserSchema(id=1, name="Alice", email="alice@example.com")
print(user)

"""
BaseModel — это базовый класс Pydantic, от которого мы наследуем нашу модель.
При создании объекта User Pydantic автоматически проверяет, что id — это число, а name и email — строки.


Если данные не соответствуют требованиям, Pydantic выбросит ошибку
"""


class ShortUserSchema(BaseModel):
    id: str
    email: str

class FullUserSchema(ShortUserSchema):
    last_name: str
    first_name: str
    middle_name: str





"""
{
  "id": "string",
  "title": "string",
  "maxScore": 0,
  "minScore": 0,
  "description": "string",
  "estimatedTime": "string"
}
"""

from pydantic import BaseModel


class CourseSchema(BaseModel):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str


# Инициализируем модель CourseSchema через передачу аргументов
"""
Мы передаем аргументы в конструктор класса CourseSchema, указывая значения для каждого поля.
Pydantic автоматически проверяет, что переданные значения соответствуют ожидаемым типам (str, int и т. д.).
При выводе в print объект отображается в виде строки, но на самом деле это Pydantic-модель, а не обычный словарь.
"""
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    estimatedTime="1 week"
)
print('Course default model:', course_default_model)





# Инициализируем модель CourseSchema через распаковку словаря
"""
Мы создали словарь course_dict, где ключи соответствуют полям CourseSchema.
Используем **course_dict для распаковки словаря, передавая его содержимое в модель.
Этот метод удобен, когда у нас уже есть данные в виде словаря, например, полученные из JSON-ответа API.
"""
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)







# Инициализируем модель CourseSchema через JSON
"""
У нас есть JSON-строка course_json.
Мы используем метод model_validate_json, который парсит строку и создает объект CourseSchema.
Это полезно, если JSON-данные хранятся в файле или приходят в виде строки от сервера.
"""

course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print('Course JSON model:', course_json_model)


# Применение на практике:
# Если у нас есть JSON-файл, мы можем загрузить его в Pydantic-модель так:

import json
with open("course.json", "r") as file:
    course_data = file.read()

course_model = CourseSchema.model_validate_json(course_data)
print(course_model)





"""  ALIAS   """
from pydantic import BaseModel, Field

class CourseSchema(BaseModel):
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
"""  Поля max_score, min_score и estimated_time теперь используют Field(alias="...").
Это позволяет использовать snake_case внутри Python-кода, но принимать camelCase-данные из API.
При создании модели, например через CourseSchema(**course_dict), \
Pydantic автоматически сопоставляет JSON-ключи с полями модели."""






"""
alias_generator для автоматического преобразования
"""
from pydantic.alias_generators import to_camel


class CourseSchema(BaseModel):
    # Автоматическое преобразование snake_case → camelCase
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

# alias_generator=to_camel автоматически превращает snake_case в camelCase.
# populate_by_name=True позволяет передавать как camelCase, так и snake_case без ошибок.
# В model_dump(by_alias=True) Pydantic сам приводит имена полей в camelCase.





