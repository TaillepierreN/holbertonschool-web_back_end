#!/usr/bin/env python3
"""
Collect 10 random numbers using an async comprehensing over async_generator,
then return the 10 random numbers.
"""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Asynchronously yield 10 random numbers, each after a 1-second delay."""
    random = [random_numbers async for random_numbers in async_generator()]
    return random
