"""Provides Hamming distance functions for sequences."""
from typing import Hashable, Sequence


def distance(s1: Sequence[Hashable], s2: Sequence[Hashable]) -> int:
    """Return the Hamming distance between equal-length sequences

    Args:
        s1:
            The first sequence to compare.
        s2:
            The second sequence to compare.

    Returns:
        int: The Hamming distance between the two sequences.

    Raises:
        ValueError: If the two sequences are not of equal length.
    """
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))
