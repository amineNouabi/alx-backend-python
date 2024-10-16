#!/usr/bin/env python3
"""

Module for 2. Run time for four parallel comprehensions.

"""

import asyncio
import random
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine will execute async_comprehension four times in parallel
        using asyncio.gather, then return the total runtime.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
