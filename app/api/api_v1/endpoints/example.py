from typing import Any, List

from fastapi import APIRouter

from app.service.example import ExampleService

router = APIRouter()


@router.get("/")
async def read_items() -> Any:
    """
    An example for get the result of bilibili's movie api
    """
    result = await ExampleService.get_example()
    return result