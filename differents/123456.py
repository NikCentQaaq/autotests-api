from http import HTTPStatus

from pydantic import BaseModel
from httpx import Response
from differents.httpx_create_user import response


class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool



response = {
    "id": 15,
    "name": "Ivan",
    "email": "ivan@test.com",
    "is_active": true
}


def assert_user_response(response: Response):
    assert response.status_code == HTTPStatus.OK
    response_model = UserResponseSchema.model_validate(**response.json())

    assert response_model.id > 15
    assert response_model.name
    assert '@' in response_model.email
    assert response_model.is_active