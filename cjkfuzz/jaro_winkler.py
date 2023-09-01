"""Provides the Jaro-Winkler similarity function"""
import os
from typing import Hashable, Sequence

from cjkfuzz import jaro


def similarity(s1: Sequence[Hashable], s2: Sequence[Hashable], p: float = 0.1) -> float:
    """Return the Jaro-Winkler similarity between two sequences

    Args:
        s1:
            The first sequence to compare.
        s2:
            The second sequence to compare.
        p:
            The prefix scaling factor. It must be between 0 and 0.25, inclusive. The default value
            is 0.1.

    Returns:
        float: The Jaro-Winkler similarity between the two sequences.

    Raises:
        ValueError: If p is not between 0 and 0.25, inclusive.
    """
    if p < 0.0 or p > 0.25:
        raise ValueError("p must be between 0 and 0.25")

    sim = jaro.similarity(s1, s2)
    prefix = len(os.path.commonprefix([s1, s2]))
    prefix_len = min(4, prefix)
    return sim + prefix_len * p * (1 - sim)
