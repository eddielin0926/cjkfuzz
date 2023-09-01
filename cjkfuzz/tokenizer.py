"""Provide tokenizer functions."""
from typing import Hashable, Sequence

from cjkfuzz import utils


def default(seq: Sequence[Hashable]) -> Sequence[Hashable]:
    """Return tokens from the sequence.

    Args:
        seq:
            The sequence to tokenize.

    Returns:
        A list of tokens.
    """
    result = [""]
    for ele in seq:
        if utils.is_cjk_char(ele):
            if result[-1] != "":
                result.append("")
            result[-1] = ele
            result.append("")
        elif ele == " " and result[-1] != "":
            result.append("")
        else:
            result[-1] += ele
    if result[-1] == "":
        result.pop()
    return result
