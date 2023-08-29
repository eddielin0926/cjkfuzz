from typing import Hashable, Sequence


def distance(s1: Sequence[Hashable], s2: Sequence[Hashable]) -> int:
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))
