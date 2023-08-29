from typing import Hashable, Sequence


def distance(s1: Sequence[Hashable], s2: Sequence[Hashable]) -> int:
    """Return the Levenshtein edit distance between two sequences"""
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
