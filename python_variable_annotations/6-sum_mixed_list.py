#!/usr/bin/env python3
"""
type-annotated function which takes a list mxd_lst of integers and floats
and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum of list of int and float as float"""
    return (sum(mxd_lst))
