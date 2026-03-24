from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, GetUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    # ... ваш существующий код ...
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


def assert_user(actual: UserSchema, expected: UserSchema):
    """Сравнение основных полей пользователя."""
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")


# Добавьте эту функцию:
def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    """Сравнивает данные из GET /me с данными, полученными при создании."""
    # Обращаемся к вложенным объектам .user в обеих схемах
    assert_user(actual=get_user_response.user, expected=create_user_response.user)








