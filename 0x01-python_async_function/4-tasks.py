#!/usr/bin/env python3
"""

Module for tasks.

"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of asyncio.Task.
    """
    return [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
