"""Модуль для проверок (assertions) упражнений."""
from clients.exercises.exercises_schema import CreateExerciseResponseSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(response_data: dict, request_data: dict):
    """
    Проверяет соответствие тела ответа данным запроса и JSON-схеме.

    :param response_data: Тело ответа (dict)
    :param request_data: Данные запроса (dict)
    """
    # Валидация JSON-схемы через Pydantic модель
    CreateExerciseResponseSchema(**response_data)

    exercise_actual = response_data["exercise"]

    assert exercise_actual["title"] == request_data["title"]
    assert exercise_actual["description"] == request_data["description"]
    assert exercise_actual["course_id"] == request_data["course_id"]
