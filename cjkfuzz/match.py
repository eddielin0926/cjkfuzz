from typing import Hashable, Sequence


def count(s1: Sequence[Hashable], s2: Sequence[Hashable]) -> int:
    result = 0
    for s in s1:
        result += s2.count(s)
    return result


def ratio(s1: Sequence[Hashable], s2: Sequence[Hashable]) -> float:
    """Return a measure of the sequences' similarity between 0 and 1"""
    max_len = max(len(s1), len(s2))
    return count(s1, s2) / max_len
