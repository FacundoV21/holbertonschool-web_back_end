#!/usr/bin/env python3
"""main function"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function to return the string representation of a float"""
    return (k, v**2)
