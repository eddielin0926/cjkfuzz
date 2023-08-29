import os
from typing import Hashable, Sequence

from cjkfuzz import jaro


def similarity(s1: Sequence[Hashable], s2: Sequence[Hashable], p: float = 0.1) -> float:
    """Return the Jaro-Winkler similarity between two sequences"""
    if p < 0.0 or p > 0.25:
        raise ValueError("p must be between 0 and 0.25")

    sim = jaro.similarity(s1, s2)
    prefix = len(os.path.commonprefix([s1, s2]))
    prefix_len = min(4, prefix)
    return sim + prefix_len * p * (1 - sim)
