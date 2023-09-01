from typing import Callable, Hashable, Sequence

from cjkfuzz import levenshtein


def ratio(
    s1: Sequence[Hashable],
    s2: Sequence[Hashable],
    processor: Callable[..., Sequence[Hashable]] = None,
    scorer: Callable[..., float] = levenshtein.ratio,
) -> float:
    """Return a measure of the sequences' similarity between 0 and 1.

    Args:
        s1: The first sequence to compare.
        s2: The second sequence to compare.
        processor: A function that pre-process the input sequences. For example, it can tokenize
            the input sequences by words or characters.
        scorer: A function that provides a measure of the similarity between two sequences and it
            should returns a float between 0 and 1, inclusive. The default scorer is the
            Levenshtein ratio.

    Returns:
        float: The similarity between the two sequences and it is between 0 and 1, inclusive.

    Raises:
        TypeError: If s1 or s2 is None.
        ValueError: If the scorer returns a value outside of the range [0, 1].
    """
    if s1 is None or s2 is None:
        raise TypeError("s1 and s2 must be non-None")
    if processor is not None:
        s1 = processor(s1)
        s2 = processor(s2)
    score = scorer(s1, s2)
    if score < 0.0 or score > 1.0:
        raise ValueError("scorer must return a value between 0 and 1")
    return score


def partial_ratio(
    s1: Sequence[Hashable],
    s2: Sequence[Hashable],
    processor: Callable[..., Sequence[Hashable]] = None,
    scorer: Callable[..., float] = levenshtein.ratio,
) -> float:
    if s1 is None or s2 is None:
        raise TypeError("s1 and s2 must be non-None")
    if processor is not None:
        s1 = processor(s1)
        s2 = processor(s2)
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    best = 0.0
    for i in range(len(s2) - len(s1) + 1):
        score = scorer(s1, s2[i : i + len(s1)])
        if score > best:
            best = score
    return best
