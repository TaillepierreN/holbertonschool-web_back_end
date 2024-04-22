#!/usr/bin/env python3
"""
type-annotated function that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """call a function to do multiplication"""
    def multiplication(value: float) -> float:
        """multiply value by multiplier"""
        return value * multiplier
    return multiplication
