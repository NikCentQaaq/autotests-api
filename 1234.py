response = {
    "status": "success",
    "data": [
        {
            "id": 1,
            "email": "ivan@test.com",
            "role": "admin",
            "is_active": True
        },
        {
            "id": 2,
            "email": "anna@test.com",
            "role": "user",
            "is_active": False
        },
        {
            "id": 3,
            "email": "kate@test.com",
            "role": "user",
            "is_active": True
        },
        {
            "id": 4,
            "email": "petr@test.com",
            "role": "admin",
            "is_active": True
        }
    ]
}



def get_active_admins(response:dict) -> list:
    try:
        assert response["status"] == "success"
    except AssertionError:
        return []

    email = []
    for us in response["data"]:
        if us['is_active'] and us['role'] == 'admin':
            email.append(us['email'])

    return email















