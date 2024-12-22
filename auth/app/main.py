from fastapi import FastAPI

from src.api import auth
from src.db.base import create_db_and_tables
from src.db.models.users import create_user_score

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    create_user_score()


app.include_router(auth.router, prefix="/authenticate", tags=["authenticate"])
