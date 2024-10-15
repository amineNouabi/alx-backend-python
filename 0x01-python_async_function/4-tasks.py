#!/usr/bin/env python3
"""

Module for tasks.

"""

import asyncio
from typing import List

task_wait_random = __import__('0-basic_async_syntax').task_wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of asyncio.Task.
    """
    delays: List[float] = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    return sorted(delays)
