#!/usr/bin/env python3

"""

Module for element length.

"""

from typing import Iterable, List, Tuple, Sequence


def element_length(
    lst: Iterable[Sequence]
) -> List[Tuple[Sequence, int]]:
    """Return the length of elements in a list."""
    return [(i, len(i)) for i in lst]
