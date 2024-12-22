import hashlib
import uuid


def generate_hashed_password(password: str) -> tuple[str, str]:
    salt = str(uuid.uuid4())
    return get_hashed_password(password, salt), salt


def get_hashed_password(password: str, salt: str) -> str:
    return hashlib.md5((password + salt).encode()).hexdigest()
