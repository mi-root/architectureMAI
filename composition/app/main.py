from fastapi import FastAPI

import src.api.login as login

app = FastAPI()

app.include_router(login.router, prefix="/login", tags=["login"])
