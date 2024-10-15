#!/usr/bin/env python3
"""

Module for tasks.

"""

from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of asyncio.Task.
    """
    delays: List[float] = []
    for _ in range(n):
        delays.append(task_wait_random(max_delay))
    return sorted(delays)
