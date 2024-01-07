#!/usr/bin/env python3
"""
    main program
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        waits x number of seconds and returns that number
    """
    await asyncio.sleep(x := random.uniform(0, max_delay))
    return x
