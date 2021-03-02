from typing import Any, List

from fastapi import APIRouter

from app.service.example import ExampleService

router = APIRouter()


@router.get("/")
async def read_items() -> Any:
    return "pong"
