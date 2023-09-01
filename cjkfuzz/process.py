"""Provide a function to extract the best matches from a list of choices"""
import bisect
from typing import Hashable, Sequence, Tuple

from cjkfuzz import fuzz


def extract(
    query: Sequence[Hashable], choices: Sequence[Sequence[Hashable]], limit: int = 1
) -> Tuple[Sequence[Hashable], int]:
    """Return a list of the best matches

    Args:
        query:
            The sequence to match.
        choices:
            The list of sequences to match against.
        limit:
            The maximum number of matches to return. The default value is 1.

    Returns:
        A tuple of the best matches and the best match's score. The best matches are sorted in
        descending order of their scores.

    Raises:
        ValueError: If limit is less than 1.
    """
    if limit < 1:
        raise ValueError("limit must be greater than 0")
    candidates = []
    for idx, choice in enumerate(choices):
        ratio = fuzz.ratio(query, choice)
        # Keep the list sorted and limit the number of candidates
        bisect.insort(candidates, (ratio, choice))
        if len(candidates) > limit:
            # Remove the worst candidate
            candidates.pop(0)
    candidates.reverse()
    return candidates
