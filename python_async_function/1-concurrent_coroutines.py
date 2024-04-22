#!/usr/bin/env python3
"""
async routine that takes in 2 int args n and max_delay
spawn wait_random() <n> times with <max_delay>
return list of all delays: float in ascending order
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
	"""async that wait <n> times and return the list of time waited"""
	time_list = [wait_random(max_delay) for wait in range(n)]
	delay_sorted_list = []
	for time in asyncio.as_completed(time_list):
		delay = await time
		delay_sorted_list.append(delay)
	return delay_sorted_list