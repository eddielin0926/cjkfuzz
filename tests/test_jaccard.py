from cjkfuzz import jaccard


def test_jaccard_distance():
    distance = jaccard.distance("中文測試", "中文測試")
    assert distance == 0


def test_jaccard_index():
    index = jaccard.index("中文測試", "中文測試")
    assert index == 1.0
