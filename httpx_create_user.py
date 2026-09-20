import httpx
from tools import fakers

payload = {
  "email": fakers.fake.email(),
  "password": "mangel",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}


response = httpx.post('http://127.0.0.1:8000/api/v1/users', json=payload)

print(response.status_code)
print(response.json())
