from cjkfuzz import fuzz


def test_fuzz_ratio() -> None:
    ratio = fuzz.ratio("中文測試", "中文測試")
    assert ratio == 1.0


def test_fuzz_partial_ratio() -> None:
    pass


def test_fuzz_token_sort_ratio() -> None:
    pass


def test_fuzz_token_set_ratio() -> None:
    pass


def test_fuzz_partial_token_sort_ratio() -> None:
    pass
