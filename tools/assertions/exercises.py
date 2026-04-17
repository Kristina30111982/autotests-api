from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, GetExerciseResponseSchema, ExerciseSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        response: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на создание задания соответствует запросу.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API с данными задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")


def assert_exercise(expected_exercise: ExerciseSchema, actual_exercise_data: dict):
    """
    Сравнивает модель упражнения с данными из ответа.
    """
    assert actual_exercise_data["id"] == expected_exercise.id
    assert actual_exercise_data["title"] == expected_exercise.title
    assert actual_exercise_data["description"] == expected_exercise.description
    assert actual_exercise_data["courseId"] == expected_exercise.course_id


def assert_get_exercise_response(response_data: dict, expected_exercise: ExerciseSchema):
    """
    Проверяет ответ GET-запроса на соответствие схеме и ожидаемым данным.
    """
    # Валидация JSON-схемы
    GetExerciseResponseSchema(**response_data)

    # Проверка данных упражнения (с учетом вложенности 'exercise')
    actual_exercise = response_data["exercise"]
    assert_exercise(expected_exercise, actual_exercise)