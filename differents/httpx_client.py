import httpx

login_payload = {
    "email": 'user@example.com',
    "password": 'string'
}

login_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print(login_response.status_code)
print('Login User Data:', login_response_data)

client = httpx.Client(
    base_url='http://127.0.0.1:8000',
    timeout=10,
    headers={'Authorization': f'Bearer {login_response_data['token']["accessToken"]}'}
)



response = client.get('/api/v1/users/me')
print(response.text)

