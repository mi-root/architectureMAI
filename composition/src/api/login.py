from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.clients import auth as auth_client
from src.clients import score as score_client
from src.config.base import settings

router = APIRouter()


class LoginRequest(BaseModel):
    login: str
    password: str


class LoginResponse(BaseModel):
    ok: bool


@router.post("/")
async def auth(login_request: LoginRequest) -> LoginResponse:
    try:
        score = await score_client.get_score(login_request.login)
        if score < settings.score_threshold:
            return LoginResponse(ok=False)
    except HTTPException as exc:
        pass

    try:
        access = await auth_client.authenticate(login_request.login, login_request.password)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Internal error: {exc}")

    return LoginResponse(ok=access)
