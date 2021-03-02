import time
import asyncio

from app.proxy.example import ExampleProxy
from app.util.time_util import timeout_log


class ExampleService:
    @classmethod
    @timeout_log(timeout=5)
    async def get_example(cls):
        example = await ExampleProxy.get_example()
        if not example:
            return {
                "example": {},
            }
        result = {
            "example": example,
        }
        return result
