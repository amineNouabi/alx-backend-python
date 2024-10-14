#!/usr/bin/env python3

"""

Module for concurrent coroutines.

"""

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays."""
    delays: List[float] = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
