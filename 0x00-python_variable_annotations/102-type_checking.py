#!/usr/bin/env python3

"""

Module for zoom_array.

"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a list with the same elements repeated by factor times."""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
