from fastapi import APIRouter
from pydantic import BaseModel

from src.db.base import SessionDep
from src.db.models.users import User
from src.utils.password import get_hashed_password

router = APIRouter()


class AuthRequest(BaseModel):
    login: str
    password: str


@router.post("/")
async def authenticate(auth_request: AuthRequest, session: SessionDep):
    user = session.get(User, auth_request.login)
    if not user or user.password != get_hashed_password(
        auth_request.password, user.salt
    ):
        return {"allowed_access": False}
    return {"allowed_access": True}
