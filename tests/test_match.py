from cjkfuzz import match


def test_match_count() -> None:
    count = match.count("中文測試", "中文測試")
    assert count == 4


def test_match_ratio() -> None:
    ratio = match.ratio("中文測試", "測試中文")
    assert ratio == 1.0
