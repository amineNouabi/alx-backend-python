#!/usr/bin/env python3
"""

Module for Basics of async syntax.

wait_random: Waits and Returns a random float delay in seconds.

"""

from random import random
from asyncio import sleep


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits and Returns
    a random float delay in seconds.
    """
    delay = random() * max_delay
    await sleep(delay)
    return delay
