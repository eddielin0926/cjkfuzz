"""Provide functions for calculating the Levenshtein edit distance"""
from typing import Hashable, Sequence


def distance(s1: Sequence[Hashable], s2: Sequence[Hashable]) -> int:
    """Return the Levenshtein edit distance between two sequences

    The Levenshtein edit distance is the minimum number of single-character edits (insertions,
    deletions or substitutions) required to change one word into the other.

    Args:
        s1:
            The first sequence to compare.
        s2:
            The second sequence to compare.

    Returns:
        int: The Levenshtein edit distance between the two sequences.

    Raises:
        TypeError: If s1 or s2 is None.
    """
    dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
    for i in range(len(s1) + 1):
        dp[0][i] = i
    for i in range(len(s2) + 1):
        dp[i][0] = i
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s1[j - 1] == s2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[-1][-1]


def ratio(s1: Sequence[Hashable], s2: Sequence[Hashable]) -> float:
    """Return a measure of the sequences' similarity between 0 and 1"""
    ldist = distance(s1, s2)
    sum_len = len(s1) + len(s2)
    return (sum_len - ldist) / sum_len
