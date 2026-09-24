users = [
    {"id": 1, "name": "Ivan"},
    {"id": 2, "name": "Anna"},
    {"id": 3, "name": "Kate"},
    {"id": 4, "name": "Petr"},
]

def find_user_by_id(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return "User not found"