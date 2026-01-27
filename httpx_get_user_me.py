import httpx


payload = {
    "email": "user1@example.com",
    "password": "ssstring"
}


response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)


print(response.status_code)
print(response.json())

headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("http://localhost:8000/api/v1/authentication/login"", headers=headers")

print(response.json())