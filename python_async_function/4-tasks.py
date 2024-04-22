#!/usr/bin/env python3
"""
async routine that takes in 2 int args n and max_delay
spawn wait_random() <n> times with <max_delay>
return list of all delays: float in ascending order
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create and manage multiple tasks that execute wait_random concurrently.
    Returns a list of the completion times in the order they finish.
    """
    tasks = [task_wait_random(max_delay) for wait in range(n)]
    delay_sorted_list = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delay_sorted_list.append(delay)
    return delay_sorted_list
