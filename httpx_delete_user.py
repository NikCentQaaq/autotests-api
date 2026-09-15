import httpx
from tools import fakers


create_user_payload = {
  "email": fakers.get_random_email(),
  "password": "mangel",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}


create_user_response = httpx.post('http://127.0.0.1:8000/api/v1/users', json=create_user_payload)

print(create_user_response.status_code)
print('Create User Data:', create_user_response.json())




login_payload = {
    "email": create_user_payload['email'],
    "password": "mangel",
}
login_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print(login_response.status_code)
print('Login User Data:', login_response_data)



delete_user_header = {
    'Authorization': f'Bearer {login_response_data['token']["accessToken"]}'
}

delete_response = httpx.delete(
    f'http://127.0.0.1:8000/api/v1/users/{create_user_response.json()['user']['id']}',
                               headers=delete_user_header)
print(delete_response.status_code)
print('Delete User Data:', delete_response.json())

