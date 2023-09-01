from cjkfuzz import fuzz


def test_fuzz_ratio() -> None:
    ratio = fuzz.ratio("中文測試", "中文測試")
    assert ratio == 1.0


def test_fuzz_partial_ratio() -> None:
    ratio = fuzz.partial_ratio("test", "more tests")
    assert ratio == 1.0
