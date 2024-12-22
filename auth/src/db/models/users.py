from sqlmodel import Field, Session, SQLModel

from src.db.base import engine
from src.utils.password import generate_hashed_password


class User(SQLModel, table=True):
    login: str = Field(primary_key=True)
    password: str
    salt: str


def create_user_score():
    with Session(engine) as session:
        password_1, salt_1 = generate_hashed_password("Abracadabra")
        user_1 = User(login="Pupkin", password=password_1, salt=salt_1)

        password_2, salt_2 = generate_hashed_password("11.09")
        user_2 = User(login="Plushkin", password=password_2, salt=salt_2)

        session.add_all([user_1, user_2])
        session.commit()
