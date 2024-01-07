#!/usr/bin/env python3
"""
   main program
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ repeats n number of delays and returns them in asc order"""
    delays: List = [wait_random(max_delay) for _ in range(n)]

    aDelays: List = await asyncio.gather(*delays)

    orgDelays: List = []

    for _ in range(n):
        min_delay = min(aDelays)
        orgDelays.append(min_delay)
        aDelays.remove(min_delay)

    return orgDelays
