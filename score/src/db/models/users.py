from sqlmodel import Field, Session, SQLModel

from src.db.base import engine


class UserScore(SQLModel, table=True):
    login: str = Field(primary_key=True)
    score: float


def create_user_score():
    with Session(engine) as session:
        user_score_1 = UserScore(login="Pupkin", score=1.0)
        user_score_2 = UserScore(login="Plushkin", score=0.1)
        session.add_all([user_score_1, user_score_2])
        session.commit()
