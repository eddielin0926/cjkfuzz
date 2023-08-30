import bisect
from typing import Hashable, Sequence, Tuple

from cjkfuzz import fuzz


def extract(
    query: Sequence[Hashable], choices: Sequence[Sequence[Hashable]], limit: int = 1
) -> Tuple[Sequence[Hashable], int]:
    """Return a list of the best matches"""
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
