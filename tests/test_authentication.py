from http import HTTPStatus
from clients.authentication.authentication_schema import LoginResponseSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


def test_login():
    """
    Тест проверяет успешную аутентификацию пользователя.
    """
    # 1. Создаем нового пользователя
    public_users_client = get_public_users_client()

    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)

    # 2. Выполняем аутентификацию (передаем email и password из созданного юзера)
    login_response = AuthenticationClient.login_api(
        email=user_data.email,
        password=user_data.password
    )

    # 3. Проверяем статус-код (200 OK)
    assert_status_code(login_response.status_code, HTTPStatus.OK)

    # 4. Десериализуем и валидируем JSON-ответ по схеме
    # model_validate_json автоматически проверит соответствие типов данных
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    # 5. Проверяем корректность логических данных в теле ответа
    assert_login_response(login_response_data)
