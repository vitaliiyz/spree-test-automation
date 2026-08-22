import os

from dotenv import load_dotenv

load_dotenv()


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Required environment variable is not set: {name}")
    return value


BASE_URL = get_required_env("BASE_URL").rstrip("/")
LOGIN_EMAIL = get_required_env("LOGIN_EMAIL")
PASSWORD = get_required_env("PASSWORD")
