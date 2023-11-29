"""Provides functions to calculate the similarity between two sequences.

The functions provide various methods to calculate the similarity between two sequences. The
similarity is between 0 and 1, inclusive. The higher the similarity, the more similar the two
sequences are. The default similarity measure is the Levenshtein ratio, but other measures can be
used as well.
"""
from typing import Callable, Hashable, Sequence

from pypinyin import lazy_pinyin

from cjkfuzz import levenshtein


def ratio(
    s1: Sequence[Hashable],
    s2: Sequence[Hashable],
    scorer: Callable[..., float] = levenshtein.ratio,
) -> float:
    """Return a measure of the sequences' similarity between 0 and 1.

    Args:
        s1:
            The first sequence to compare.
        s2:
            The second sequence to compare.
        scorer:
            A function that provides a measure of the similarity between two sequences and it
            should returns a float between 0 and 1, inclusive. The default scorer is the Levenshtein
            ratio.

    Returns:
        float: The similarity between the two sequences and it is between 0 and 1, inclusive.

    Raises:
        TypeError: If s1 or s2 is None.
    """
    if s1 is None or s2 is None:
        raise TypeError("s1 and s2 must be non-None")
    s1 = lazy_pinyin(s1)
    s2 = lazy_pinyin(s2)
    score = scorer(s1, s2)
    return score


def partial_ratio(
    s1: Sequence[Hashable],
    s2: Sequence[Hashable],
    scorer: Callable[..., float] = levenshtein.ratio,
) -> float:
    """Return a measure of the sequences' similarity between 0 and 1.

    Partial ratio is similar to ratio, but it only consider the best matching substring of s1 and
    s2. For example, if s1 is "abcd" and s2 is "abcdef", then the partial ratio is 1.0.

    Args:
        s1:
            The first sequence to compare.
        s2:
            The second sequence to compare.
        scorer:
            A function that provides a measure of the similarity between two sequences and it
            should returns a float between 0 and 1, inclusive. The default scorer is the Levenshtein
            ratio.

    Returns:
        float: The similarity between the two sequences and it is between 0 and 1, inclusive.

    Raises:
        TypeError: If s1 or s2 is None.
    """
    if s1 is None or s2 is None:
        raise TypeError("s1 and s2 must be non-None")
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    s1 = lazy_pinyin(s1)
    s2 = lazy_pinyin(s2)
    best = scorer(s1, s2)
    # TODO: Use a better algorithm to find the best matching substring.
    for i in range(len(s1), len(s2)):
        for j in range(len(s2) - i + 1):
            score = scorer(s1, s2[j : j + i])
            if score > best:
                best = score
    return best
