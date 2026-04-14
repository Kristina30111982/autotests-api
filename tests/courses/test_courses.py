from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.courses import CourseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_create_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_update_course(self, courses_client: CoursesClient, function_course: CourseFixture):
        # Формируем данные для обновления
        request = UpdateCourseRequestSchema()
        # Отправляем запрос на обновление курса
        response = courses_client.update_course_api(function_course.response.course.id, request)
        # Преобразуем JSON-ответ в объект схемы
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        # Проверяем статус-код ответа
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что данные в ответе соответствуют запросу
        assert_update_course_response(request, response_data)

        # Валидируем JSON-схему ответа
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_create_course(self, courses_client: CoursesClient, function_file, function_user):
        """
        Тест на успешное создание курса через API.
        """
        # 1. Формируем объект запроса
        request_data = CreateCourseRequestSchema(
            title="Автоматизация на Python",
            description="Курс по API тестированию",
            preview_file_id=function_file.response.file.id,
            created_by_user_id=function_user.response.user.id
        )

        # 2. Вызываем метод (он возвращает CreateCourseResponseSchema)
        response_model = courses_client.create_course(request=request_data)

        # 3. Проверка тела ответа через функцию-ассерт
        # Превращаем модель ответа в dict для ассерта, используя model_dump() или .dict()
        assert_create_course_response(
            response_data=response_model.model_dump(),
            request_data=request_data.model_dump()
        )