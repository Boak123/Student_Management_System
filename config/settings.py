import os
from dotenv import load_dotenv

load_dotenv()


APP_NAME = "Student Management System"
UNIVERSITY_NAME = "KWASU"

PASSING_SCORE = 50
MAX_STUDENTS = 1000

CURRENT_SESSION = "2026/2027"
DEFAULT_LEVEL = "100L"

DEBUG = os.getenv("DEBUG", "False") == "True"

SECRET_KEY = os.getenv("SECRET_KEY")
