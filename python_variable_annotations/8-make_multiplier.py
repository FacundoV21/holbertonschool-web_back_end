#!/usr/bin/env python3
"""main function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplies float"""
    return lambda x: x * multiplier
