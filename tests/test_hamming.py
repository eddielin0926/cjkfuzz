import pytest

from cjkfuzz import hamming


def test_hamming_distance():
    distance = hamming.distance("中文測試", "中文測試")
    assert distance == 0


def test_hamming_distance_non_equal_length():
    with pytest.raises(ValueError):
        hamming.distance("not", "equal")
