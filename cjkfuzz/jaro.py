"""Provides the Jaro similarity function"""
from typing import Hashable, Sequence


def similarity(s1: Sequence[Hashable], s2: Sequence[Hashable]) -> float:
    """Return the Jaro similarity between two sequences

    The Jaro similarity is a measure of similarity between two strings. The higher the Jaro
    similarity for two strings is, the more similar the strings are. The Jaro similarity is between
    0 and 1, inclusive. The Jaro similarity is defined as:

    .. math::
        \\frac{1}{3} \\left(\\frac{m}{|s_1|} + \\frac{m}{|s_2|} + \\frac{m - t}{m}\\right)

    where :math:`m` is the number of matching characters, :math:`t` is the number of transpositions,
    :math:`|s_1|` is the length of the first string, and :math:`|s_2|` is the length of the second
    string.

    Args:
        s1:
            The first sequence to compare.
        s2:
            The second sequence to compare.

    Returns:
        float: The Jaro similarity between the two sequences.

    Raises:
        ValueError: If the two sequences are of zero length.
    """
    s1_len = len(s1)
    s2_len = len(s2)

    if s1_len == 0 or s2_len == 0:
        raise ValueError("Undefined for sequences of zero length")

    max_dist = max(s1_len, s2_len) // 2 - 1

    s1_matches = [False] * s1_len
    s2_matches = [False] * s2_len

    matches = 0
    transpositions = 0

    for i in range(s1_len):
        start = max(0, i - max_dist)
        end = min(i + max_dist + 1, s2_len)

        for j in range(start, end):
            if s2_matches[j]:
                continue
            if s1[i] != s2[j]:
                continue
            s1_matches[i] = True
            s2_matches[j] = True
            matches += 1
            break

    if matches == 0:
        return 0.0

    k = 0
    for i in range(s1_len):
        if not s1_matches[i]:
            continue
        while not s2_matches[k]:
            k += 1
        if s1[i] != s2[k]:
            transpositions += 1
        k += 1

    return (matches / s1_len + matches / s2_len + (matches - transpositions / 2) / matches) / 3
