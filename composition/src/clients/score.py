import urllib.parse

import aiohttp
from fastapi import HTTPException

from src.config.base import settings


async def get_score(login: str) -> float:
    async with aiohttp.ClientSession(settings.score_url, trust_env=True) as session:
        try:
            async with session.get(
                "/score", params={"login": login}, ssl=False
            ) as response:
                if response.status != 200:
                    detail = await response.text()
                    raise HTTPException(status_code=response.status, detail=detail)

                data = await response.json()
                score = data["score"]
        except aiohttp.ClientError as exc:
            raise HTTPException(status_code=500, detail=f"Failed score request: {exc}")
    return score
