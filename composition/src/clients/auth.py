import aiohttp
from fastapi import HTTPException

from src.config.base import settings


async def authenticate(login: str, password: str) -> bool:
    async with aiohttp.ClientSession(settings.auth_url) as session:
        try:
            async with session.post(
                "/authenticate", json={"login": login, "password": password}
            ) as response:
                if response.status != 200:
                    detail = await response.text()
                    raise HTTPException(status_code=response.status, detail=detail)

                data = await response.json()
                access_allowed = data["allowed_access"]
        except aiohttp.ClientError as exc:
            raise HTTPException(status_code=500, detail=f"Failed auth request: {exc}")
    return access_allowed
