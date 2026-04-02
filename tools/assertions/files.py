from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileResponseSchema, CreateFileRequestSchema, FileSchema, GetFileResponseSchema
from tools.assertions.base import assert_equal, assert_validation_error_response
from tools.assertions.errors import assert_validation_error_response


def assert_file(actual: FileSchema, expected: FileSchema):
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")


def assert_create_file_response(
        actual_response: CreateFileResponseSchema,
        expected_request: CreateFileRequestSchema
):
    # Проверяем, что созданный файл соответствует тому, что мы отправляли
    assert_equal(actual_response.filename, expected_request.filename, "filename")
    assert_equal(actual_response.directory, expected_request.directory, "directory")


def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    # ВАЖНО: Дописываем вызов assert_file.
    # Предполагаю, что в GetFileResponseSchema объект файла лежит в поле .file
    assert_file(get_file_response.file, create_file_response.file)


def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",  # Тип ошибки, связанной с слишком короткой строкой.
                input="",  # Пустое имя файла.
                context={"min_length": 1},  # Минимальная длина строки должна быть 1 символ.
                message="String should have at least 1 character",  # Сообщение об ошибке.
                location=["body", "filename"]  # Ошибка возникает в теле запроса, поле "filename".
            )
        ]
    )
    assert_validation_error_response(actual, expected)


def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",  # Тип ошибки, связанной с слишком короткой строкой.
                input="",  # Пустая директория.
                context={"min_length": 1},  # Минимальная длина строки должна быть 1 символ.
                message="String should have at least 1 character",  # Сообщение об ошибке.
                location=["body", "directory"]  # Ошибка возникает в теле запроса, поле "directory".
            )
        ]
    )
    assert_validation_error_response(actual, expected)


def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Проверяет, что ответ API соответствует ошибке 'File not found'.
    """
    expected_details = "File not found"

    # Сравниваем поле details из пришедшего ответа с ожидаемой строкой
    assert_equal(actual.details, expected_details, "error details")


def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что API возвращает специфическую ошибку валидации UUID при передаче некорректного file_id.
    """
    expected_detail = [
        {
            "type": "uuid_parsing",
            "loc": [
                "path",
                "file_id"
            ],
            "msg": "Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
            "input": "incorrect-file-id",
            "ctx": {
                "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
            }
        }
    ]

    # Создаем ожидаемую модель для сравнения
    expected = ValidationErrorResponseSchema(detail=expected_detail)

    # Вызываем базовый ассерт, который сравнивает .details (или .detail в зависимости от вашей схемы)
    assert_validation_error_response(actual, expected)
