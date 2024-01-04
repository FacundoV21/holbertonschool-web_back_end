#!/usr/bin/env python3
"""main function"""

from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns something"""
    return [(i, len(i)) for i in lst]
