#!/usr/bin/env python3

"""

Module for element length.

"""

from typing import Sequence, Union, Any, List, Tuple


def element_length(
    lst: Sequence[Union[Sequence[Any], str]]
) -> List[Tuple[Sequence[Any], int]]:
    """Return the length of elements in a list."""
    return [(i, len(i)) for i in lst]
