#!/usr/bin/env python3
"""
coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously yield 10 random numbers, each after a 1-second delay."""
    for num in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
