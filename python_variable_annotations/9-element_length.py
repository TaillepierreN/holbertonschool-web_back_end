#!/usr/bin/env python3
"""
type annoted function to return lenght element in list
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples, where each tuple contains an element from 'lst'
    and its length.
    Each element in 'lst' must be a sequence (e.g., list, string, tuple)."""
    return [(i, len(i)) for i in lst]
