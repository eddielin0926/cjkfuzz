"""Provides Jaccard index and distance functions."""
from typing import Hashable, Sequence


def index(s1: Sequence[Hashable], s2: Sequence[Hashable]) -> float:
    """Return the Jaccard index between two sequences

    The Jaccard index is a measure of similarity between two sequences. It is defined as the
    cardinality of the intersection divided by the cardinality of the union of the two sets.

    .. math:: J(A, B) = \\frac{|A \\cap B|}{|A \\cup B|}
    .. math:: 0 \\leq J(A, B) \\leq 1

    Args:
        s1:
            The first sequence to compare.
        s2:
            The second sequence to compare.

    Returns:
        float: The Jaccard index between the two sequences.

    Raises:
        TypeError: If s1 or s2 is None.
    """
    s1 = set(s1)
    s2 = set(s2)
    return len(s1 & s2) / len(s1 | s2)


def distance(s1: Sequence[Hashable], s2: Sequence[Hashable]) -> int:
    """Return the Jaccard distance between two sequences

    The Jaccard distance is the minimum number of single-character edits (insertions,
    deletions or substitutions) required to change one word into the other.

    .. math::
        d_{Jaccard}(A, B) = 1 - J(A, B) = 1 - \\frac{|A \\cup B| - |A \\cap B|}{|A \\cup B|}

    Args:
        s1:
            The first sequence to compare.
        s2:
            The second sequence to compare.

    Returns:
        int: The Jaccard distance between the two sequences.

    Raises:
        TypeError: If s1 or s2 is None.
    """
    s1 = set(s1)
    s2 = set(s2)
    return len(s1 | s2) - len(s1 & s2)
