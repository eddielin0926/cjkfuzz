from typing import Hashable, Sequence

from cjkfuzz import levenshtein


def ratio(s1: Sequence[Hashable], s2: Sequence[Hashable]) -> float:
    """Return a measure of the sequences' similarity between 0 and 1"""
    return levenshtein.ratio(s1, s2)
