"""Provide a function to extract the best matches from a list of choices"""
import bisect
from typing import Callable, Hashable, Sequence, Tuple

from cjkfuzz import levenshtein


def extract(
    query: Sequence[Hashable],
    choices: Sequence[Sequence[Hashable]],
    limit: int = 1,
    scorer: Callable[..., float] = levenshtein.ratio,
) -> Tuple[Sequence[Hashable], int]:
    """Return a list of the best matches

    Args:
        query:
            The sequence to match.
        choices:
            The list of sequences to match against.
        limit:
            The maximum number of matches to return. The default value is 1.
        scorer:
            A function that provides a measure of the similarity between two sequences and it
            should returns a float between 0 and 1, inclusive. The default scorer is the Levenshtein
            ratio.

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
        score = scorer(query, choice)
        # Keep the list sorted and limit the number of candidates
        bisect.insort(candidates, (score, choice))
        if len(candidates) > limit:
            # Remove the worst candidate
            candidates.pop(0)
    candidates.reverse()
    return candidates
