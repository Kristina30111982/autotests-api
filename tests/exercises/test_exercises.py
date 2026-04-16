import pytest
from http import HTTPStatus
from clients.exercises.exercises_client import ExercisesClient
from tools.assertions.exercises import assert_create_exercise_response
from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    """Класс с тестами для упражнений."""

    def test_create_exercise(self, exercises_client: ExercisesClient, function_course):
        """
        Тест на успешное создание упражнения.

        Шаги:
        1. Сформировать данные для создания упражнения.
        2. Выполнить POST запрос /api/v1/exercises.
        3. Проверить статус-код 200.
        4. Проверить тело ответа и JSON-схему.
        """
        request_data = CreateExerciseRequestSchema(
            title="Новое упражнение",
            description="Описание тестового упражнения",
            course_id=function_course.response.course.id
        )

        # Выполнение запроса
        response_model = exercises_client.create_exercise(request=request_data)

        # 3. Проверка тела ответа через функцию-ассерт
        # Превращаем модель ответа в dict для ассерта, используя model_dump() или .dict()
        assert_create_exercise_response(
            response_data=response_model.model_dump(),
            request_data=request_data.model_dump()
        )





