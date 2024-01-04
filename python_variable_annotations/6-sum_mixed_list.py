#!/usr/bin/env python3
"""main function"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function to return the string representation of a float"""
    sum = 0
    for x in mxd_lst:
        sum += x
    return float(sum)
