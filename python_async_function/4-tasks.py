#!/usr/bin/env python3
"""
    main function
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ returns the delays in asc order """
    delays: List = [task_wait_random(max_delay) for _ in range(n)]

    aDelays: List = await asyncio.gather(*delays)
    sDelays: List = []

    for i in range(n):
        minDelay = min(aDelays)
        sDelays.append(minDelay)
        aDelays.remove(minDelay)

    return sDelays
