"""Provides functions to calculate the similarity between two sequences.

The functions provide various methods to calculate the similarity between two sequences. The
similarity is between 0 and 1, inclusive. The higher the similarity, the more similar the two
sequences are. The default similarity measure is the Levenshtein ratio, but other measures can be
used as well.
"""
from typing import Callable, Hashable, Sequence

from cjkfuzz import levenshtein, tokenizer


def ratio(
    s1: Sequence[Hashable],
    s2: Sequence[Hashable],
    preprocess: Callable[..., Sequence[Hashable]] = None,
    scorer: Callable[..., float] = levenshtein.ratio,
) -> float:
    """Return a measure of the sequences' similarity between 0 and 1.

    Args:
        s1:
            The first sequence to compare.
        s2:
            The second sequence to compare.
        preprocess:
            A function that pre-process the input sequences. For example, it can change the chinese
            characters to their pinyin representations.
        scorer:
            A function that provides a measure of the similarity between two sequences and it
            should returns a float between 0 and 1, inclusive. The default scorer is the Levenshtein
            ratio.

    Returns:
        float: The similarity between the two sequences and it is between 0 and 1, inclusive.

    Raises:
        TypeError: If s1 or s2 is None.
        ValueError: If the scorer returns a value outside of the range [0, 1].
    """
    if s1 is None or s2 is None:
        raise TypeError("s1 and s2 must be non-None")
    if preprocess is not None:
        s1 = preprocess(s1)
        s2 = preprocess(s2)
    score = scorer(s1, s2)
    if score < 0.0 or score > 1.0:
        raise ValueError("scorer must return a value between 0 and 1")
    return score


def partial_ratio(
    s1: Sequence[Hashable],
    s2: Sequence[Hashable],
    preprocess: Callable[..., Sequence[Hashable]] = None,
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
        preprocess:
            A function that pre-process the input sequences. For example, it can change the chinese
            characters to their pinyin representations.
        scorer:
            A function that provides a measure of the similarity between two sequences and it
            should returns a float between 0 and 1, inclusive. The default scorer is the Levenshtein
            ratio.

    Returns:
        float: The similarity between the two sequences and it is between 0 and 1, inclusive.

    Raises:
        TypeError: If s1 or s2 is None.
        ValueError: If the scorer returns a value outside of the range [0, 1].
    """
    if s1 is None or s2 is None:
        raise TypeError("s1 and s2 must be non-None")
    if preprocess is not None:
        s1 = preprocess(s1)
        s2 = preprocess(s2)
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    best = 0.0
    for i in range(len(s2) - len(s1) + 1):
        score = scorer(s1, s2[i : i + len(s1)])
        if score > best:
            best = score
    return best


def token_sort_ratio(
    s1: Sequence[Hashable],
    s2: Sequence[Hashable],
    preprocess: Callable[..., Sequence[Hashable]] = None,
    tokenizer: Callable[..., Sequence[Hashable]] = tokenizer.default,
    scorer: Callable[..., float] = levenshtein.ratio,
) -> float:
    """Return a measure of the sequences' similarity between 0 and 1.

    Token sort ratio is similar to ratio, but it sorts the tokens in the input sequences before
    comparing them. For example, if s1 is "token sort" and s2 is "sort token", then the token sort
    ratio is 1.0.

    Args:
        s1:
            The first sequence to compare.
        s2:
            The second sequence to compare.
        preprocess:
            A function that pre-process the input sequences. For example, it can change the chinese
            characters to their pinyin representations.
        tokenizer:
            A function that tokenizes the input sequences. The default tokenizer is the default
            tokenizer in the tokenizer module.
        scorer:
            A function that provides a measure of the similarity between two sequences and it
            should returns a float between 0 and 1, inclusive. The default scorer is the Levenshtein
            ratio.

    Returns:
        float: The similarity between the two sequences and it is between 0 and 1, inclusive.

    Raises:
        TypeError: If s1 or s2 is None.
        ValueError: If the scorer returns a value outside of the range [0, 1].
    """
    if s1 is None or s2 is None:
        raise TypeError("s1 and s2 must be non-None")
    if tokenizer is None:
        raise TypeError("preprocess must be non-None")
    if preprocess is not None:
        s1 = preprocess(s1)
        s2 = preprocess(s2)
    s1 = sorted(tokenizer(s1))
    s2 = sorted(tokenizer(s2))
    print(s1, s2)
    return scorer(sorted(s1), sorted(s2))
