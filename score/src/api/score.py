from fastapi import APIRouter, HTTPException

from src.db.base import SessionDep
from src.db.models.users import UserScore

router = APIRouter()


@router.get("/")
async def score(login, session: SessionDep):
    user_score = session.get(UserScore, login)
    if not user_score:
        raise HTTPException(status_code=404, detail="User not found")
    return {"score": user_score.score}
