from sqlmodel import Session, SQLModel, create_engine

from src.config.base import settings

engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
