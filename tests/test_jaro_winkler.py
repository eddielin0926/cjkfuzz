import pytest

from cjkfuzz import jaro_winkler


def test_jaro_winkler_similarity() -> None:
    similarity = jaro_winkler.similarity("This is an arbitrary sentence", "It is an random string")
    assert similarity == pytest.approx(0.6138322884012539)


def test_jaro_similarity_invalid() -> None:
    with pytest.raises(ValueError):
        jaro_winkler.similarity("", "", p=0.26)
