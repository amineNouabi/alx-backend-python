#!/usr/bin/env python3

"""

Module for to kv.

"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing a string and a float."""
    return (k, v ** 2)
