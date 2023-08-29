from cjkfuzz import hamming


def test_hamming_distance():
    distance = hamming.distance("中文測試", "中文測試")
    assert distance == 0
