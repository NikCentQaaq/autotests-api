from enum import Enum
# конкретные сценарии, которые можно выполнять в рамках каждой фичи

class AllureStory(str, Enum):
    LOGIN = "Login"

    GET_ENTITY = "Get entity"
    GET_ENTITIES = "Get entities"
    CREATE_ENTITY = "Create entity"
    UPDATE_ENTITY = "Update entity"
    DELETE_ENTITY = "Delete entity"
    VALIDATE_ENTITY = "Validate entity"