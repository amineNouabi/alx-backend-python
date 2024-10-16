#!/usr/bin/env python3
"""

Module for 0. Async Generator

"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async generator that yields a random
        number between 0 and 10 every 1 second"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
