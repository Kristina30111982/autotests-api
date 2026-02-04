from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateRequestDict(TypedDict):
    """
    Клиент для работы с /api/v1/users
    Описание структуры запроса для создания пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    def create_user_api(self, request: CreateRequestDict) -> Response:
        """
            Метод выполняет создание пользователя.

            :param request: Словарь с email password lastName firstName middleName.
            :return: Ответ от сервера в виде объекта httpx.Response
            """
        return self.post("api/v1/users", json=request)
