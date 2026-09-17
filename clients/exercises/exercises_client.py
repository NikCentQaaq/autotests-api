from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None



class Exercises(TypedDict):
    """
    Описание структуры Упражнения
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class ExercisesResponse(TypedDict):
    """
    Описание структуры ответа получения курса.
    """
    exercise: Exercises




class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка заданий. ПО ID КУРСА

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)


    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания. ПО ID ЗАДАНИЯ

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")


    def get_exercise(self, exercise_id: str) -> ExercisesResponse:
        # Инициализируем Получение задания по ID
        response = self.get_exercise_api(exercise_id)
        # Возвращается JSON-ответ
        return response.json()


    def get_exercises(self, query: GetExercisesQueryDict) -> ExercisesResponse:
        # Инициируем Получение заданий КУРСА
        response = self.get_exercises_api(query)
        # Возвращается JSON-ответ
        return response.json()





    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)



    def create_exercise(self, request: CreateExerciseRequestDict) -> ExercisesResponse:
        # Инициируем Создание курса
        response = self.create_exercise_api(request)
        # Возвращается JSON-ответ
        return response.json()



    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)


    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> ExercisesResponse:
        # Инициируем частичное Обновление курса
        response = self.update_exercise_api(exercise_id, request)
        # Возвращается JSON-ответ
        return response.json()




    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")







def get_exercise_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))