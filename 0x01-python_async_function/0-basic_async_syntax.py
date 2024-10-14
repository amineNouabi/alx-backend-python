#!/usr/bin/env python3
"""

Module for basic async syntax.

"""

from random import uniform
from asyncio import sleep


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits and Returns a random float delay in seconds.
    """
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay
