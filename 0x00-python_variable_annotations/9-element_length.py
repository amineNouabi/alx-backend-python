#!/usr/bin/env python3

"""

Module for element length.

"""

from typing import Sequence, Union, Any, List


def element_length(
        lst: Sequence[Union[Sequence[Any], Any]]
) -> List[int]:
    """Return the length of elements in a sequence."""
    return [len(i) for i in lst]
