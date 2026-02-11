from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class UpdateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление пользователя.
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def get_user_me_api(self) -> Response:
        """
        Метод получения текущего пользователя.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получения пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")



# С паттерном Facade все API вызовы инкапсулируются в один класс:
# class UsersClient:
#     def __init__(self, base_url: str):
#         self.client = httpx.Client(base_url=base_url)
#
#     def get_user(self, user_id: str):
#         return self.client.get(f"/api/v1/users/{user_id}")
#
#     def update_user(self, user_id: str, data: dict):
#         return self.client.patch(f"/api/v1/users/{user_id}", json=data)
#
#     def delete_user(self, user_id: str):
#         return self.client.delete(f"/api/v1/users/{user_id}")

# Теперь клиентский код выглядит чисто и понятно:
# client = UsersClient(base_url="https://example.com")
#
# response = client.get_user(user_id)
# response = client.update_user(user_id, {"email": "new@example.com"})
# response = client.delete_user(user_id)
