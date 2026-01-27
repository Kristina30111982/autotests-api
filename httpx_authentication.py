import httpx  # Импортируем библиотеку HTTPX

# Инициализируем JSON-данные, которые будем отправлять в API
login_payload = {
    "email": "user@youexample.com",
    "password": "string456"
}

# Выполняем POST-запрос к эндпоинту /api/v1/authentication/login
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status code:", login_response.status_code)

refresh_payload = {
  "refreshToken": login_response_data["token"]["refreshToken"]
}

refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

print("Refresh response:",refresh_response_data )
print("Status code:", refresh_response.status_code)