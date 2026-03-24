import pytest
from http import HTTPStatus
from clients.users.users_schema import GetUserResponseSchema
from tools.assertions.users import assert_get_user_response


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(private_users_client, function_user):
    # 1. Отправляем запрос
    response = private_users_client.get_user_me_api()

    # 2. Проверяем статус-код
    assert response.status_code == HTTPStatus.OK

    # 3. Валидируем JSON схему и преобразуем в модель
    # (Предполагается, что .json() возвращает данные, а модель умеет валидировать)
    response_data = GetUserResponseSchema(**response.json())

    # 4. Проверяем корректность тела ответа
    assert_get_user_response(
        get_user_response=response_data,
        create_user_response=function_user.response
    )
