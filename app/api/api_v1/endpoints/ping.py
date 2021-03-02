from typing import String

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def ping() -> String:
    return "pong"
