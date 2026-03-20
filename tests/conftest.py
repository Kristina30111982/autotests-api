import pytest  # Импортируем pytest

# Импортируем API клиенты
from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def authentication_client() -> AuthenticationClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с аутентификацией
    return get_authentication_client()


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def public_users_client() -> PublicUsersClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с публичным API пользователей
    return get_public_users_client()
