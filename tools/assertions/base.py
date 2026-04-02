from typing import Any, Sized


def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус-код.
    :raises AssertionError: Если статус-коды не совпадают.
    """
    assert actual == expected, (
        f'Incorrect response status code. '
        f'Expected status code: {expected}. '
        f'Actual status code: {actual}'
    )


def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """
    assert actual == expected, (
        f'Incorrect value: "{name}". '
        f'Expected value: {expected}. '
        f'Actual value: {actual}'
    )


def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    assert len(actual) == len(expected), (
        f'Incorrect object length: "{name}". '
        f'Expected length: {len(expected)}. '
        f'Actual length: {len(actual)}'
    )


def assert_validation_error_response(response, expected_detail: list[dict[str, Any]]):
    """
    Проверяет, что API возвращает ошибку валидации с ожидаемым содержанием.

    :param response: Объект ответа от API.
    :param expected_detail: Ожидаемый список ошибок в ключе 'detail'.
    """
    response_json = response.json()

    # Сначала проверяем наличие ключа 'detail'
    assert "detail" in response_json, (
        f"Response body does not contain 'detail' key. "
        f"Actual response: {response_json}"
    )

    actual_detail = response_json["detail"]

    # Сравниваем фактический список ошибок с ожидаемым
    assert actual_detail == expected_detail, (
        f"Incorrect validation error detail. \n"
        f"Expected: {expected_detail} \n"
        f"Actual: {actual_detail}"
    )