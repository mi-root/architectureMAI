from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Composition App"
    score_url: str
    auth_url: str
    score_threshold: float

    class Config:
        env_file = ".env"


settings = Settings()
