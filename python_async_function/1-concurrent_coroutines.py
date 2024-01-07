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

    for i in range(n):
        mDelay = min(aDelays)
        orgDelays.append(mDelay)
        aDelays.remove(mDelay)

    return orgDelays
