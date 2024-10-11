#!/usr/bin/env python3

"""

Module for multiplying two floats.

"""


def make_multiplier(multiplier: float) -> callable:
    """Return a function that multiplies a float by multiplier."""
    def multiplier_fn(n: float) -> float:
        """Return the product of n and multiplier."""
        return n * multiplier
    return multiplier_fn
