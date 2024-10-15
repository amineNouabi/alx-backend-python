#!/usr/bin/env python3
"""

Module for Basics of async syntax.

"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits and Returns a random float delay in seconds.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
