import httpx

login_payload = {
    "email": "mmm@mail.ru",
    "password": "mangel",
}

login_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=login_payload)

login_response_data = login_response.json()

print('Login Response Data:', login_response_data)
print(login_response.status_code)

# refresh_payload = {
#     "refreshToken": login_response_data['token']['refreshToken']
# }
# refresh_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/refresh', json=refresh_payload)
# refresh_response_data = refresh_response.json()
# print('Refresh Response Data:', refresh_response_data)
# print(refresh_response.status_code)

headers = {
    "Authorization": f"Bearer {login_response_data['token']['refreshToken']}"
}
users_me_response = httpx.get('http://127.0.0.1:8000/api/v1/users/me', headers=headers)
users_me_response_data = users_me_response.json()
print(users_me_response_data)
print(users_me_response.status_code)













