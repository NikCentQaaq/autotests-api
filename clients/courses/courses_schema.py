from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake

class GetCoursesQuerySchema(BaseModel):
    model_config = ConfigDict(validate_by_alias=True,
                              validate_by_name=True)
    """
    Описание структуры запроса на получение списка курсов.
    """
    user_id: str = Field(alias="userId")


class CreateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(validate_by_alias=True,
                              validate_by_name=True)
    """
    Описание структуры запроса на создание курса.
    """
    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)


class UpdateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(validate_by_alias=True,
                              validate_by_name=True)
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int| None = Field(alias="minScore", default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class CourseSchema(BaseModel):
    model_config = ConfigDict(validate_by_alias=True,
                              validate_by_name=True)
    """
    Описание структуры курса.
    """
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile") # Вложенная структура файла
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")  # Вложенная структура пользователя

class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema

