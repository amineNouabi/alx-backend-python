#!/usr/bin/env python3
"""

Module for tasks.

"""

import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return the list of all the delays.
    """
    return asyncio.run(wait_n(n, max_delay))
