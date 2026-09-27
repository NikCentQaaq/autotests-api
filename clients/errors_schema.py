from typing import Any

from pydantic import BaseModel, Field, ConfigDict

"""
Ошибки валидации имеют единый формат во всех эндпоинтах API. 
= создаем Универсальную схему обработки ошибок
"""

class ValidationErrorSchema(BaseModel):
    """
    Модель, описывающая структуру ошибки валидации API.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    type: str
    input: Any
    context: dict[str, Any] = Field(alias="ctx")
    message: str = Field(alias="msg")
    location: list[str] = Field(alias="loc")



class ValidationErrorResponseSchema(BaseModel):
    """
    Модель, описывающая СТРУКТУРА ОТВЕТА API с ошибкой валидации.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    details: list[ValidationErrorSchema] = Field(alias="detail")







class InternalErrorResponseSchema(BaseModel):
    """
    Модель для описания внутренней ошибки.
    """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    details: str = Field(alias="detail")
