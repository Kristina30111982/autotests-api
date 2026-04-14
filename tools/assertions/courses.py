from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CreateCourseResponseSchema
from tools.assertions.base import assert_equal


def assert_update_course_response(
        request: UpdateCourseRequestSchema,
        response: UpdateCourseResponseSchema
):
    """
    Проверяет, что ответ на обновление курса соответствует данным из запроса.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API с обновленными данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")


def assert_create_course_response(response_data: dict, request_data: dict):
    """
    Проверяет соответствие тела ответа данным запроса и JSON-схеме.
    """
    # Теперь это сработает, так как схема импортирована
    CreateCourseResponseSchema(**response_data)

    # ВАЖНО: Судя по логу, ваш ответ имеет вложенность ["course"]
    # response_data = {'course': {'title': '...', ...}}
    course_actual = response_data["course"]

    assert course_actual["title"] == request_data["title"]
    assert course_actual["description"] == request_data["description"]

    # Проверка вложенных ID
    assert course_actual["preview_file"]["id"] == request_data["preview_file_id"]
    assert course_actual["created_by_user"]["id"] == request_data["created_by_user_id"]
