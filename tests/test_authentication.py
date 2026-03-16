from http import HTTPStatus

from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from clients.authentication.authentication_client import get_authentication_client
from clients.public_http_builder import get_public_http_client


def test_login():
    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()

    # создаем пользователя
    created_user = public_users_client.create_user()

    # логинимся
    login_response = authentication_client.login_api(
        email=create_user_request.email,
        password=create_user_request.password
    )

    # проверка status code
    assert_status_code(login_response.status_code, HTTPStatus.OK)

    # десериализация ответа
    login_response_data = LoginResponseSchema.model_validate_json(
        login_response.text
    )

    # проверка тела ответа
    assert_login_response(login_response_data)