from enum import Enum
# ключевые функциональные блоки нашей системы

class AllureFeature(str, Enum):
    USERS = "Users"
    FILES = "Files"
    COURSES = "Courses"
    EXERCISES = "Exercises"
    AUTHENTICATION = "Authentication"