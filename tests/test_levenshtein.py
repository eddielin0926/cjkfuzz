from cjkfuzz import levenshtein


def test_levenshtein_distance():
    distance = levenshtein.distance("中文測試", "中文測試")
    assert distance == 0


def test_levenshtein_ratio():
    ratio = levenshtein.ratio("中文測試", "中文測試")
    assert ratio == 1.0
