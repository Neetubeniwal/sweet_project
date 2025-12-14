import requests

API_URL = "http://127.0.0.1:8000"

res = requests.post(f"{API_URL}/auth/register", json={
    "username": "testuser",
    "email": "test@example.com",
    "password": "123456"
})
print("Register:", res.status_code, res.text)

res = requests.post(f"{API_URL}/auth/login", json={
    "email": "test@example.com",
    "password": "123456"
})
print("Login:", res.status_code, res.text)
