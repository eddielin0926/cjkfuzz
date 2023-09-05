import pytest

from cjkfuzz import fuzz


def test_fuzz_ratio() -> None:
    ratio = fuzz.ratio("中文測試", "中文測試")
    assert ratio == 1.0


def test_fuzz_ratio_preprocess() -> None:
    ratio = fuzz.ratio("中文測試", "中文測試", preprocess=lambda x: x)
    assert ratio == 1.0


def test_fuzz_ratio_scorer() -> None:
    with pytest.raises(ValueError):
        fuzz.ratio("中文測試", "中文測試", scorer=lambda x, y: 2.0)


def test_fuzz_ratio_none() -> None:
    with pytest.raises(TypeError):
        fuzz.ratio(None, None)


def test_fuzz_partial_ratio() -> None:
    ratio = fuzz.partial_ratio("test", "more tests")
    assert ratio == 1.0


def test_fuzz_partial_ratio_preprocess() -> None:
    ratio = fuzz.partial_ratio("more tests", "test", preprocess=lambda x: x)
    assert ratio == 1.0


def test_fuzz_partial_ratio_none() -> None:
    with pytest.raises(TypeError):
        fuzz.partial_ratio(None, None)


def test_token_sort_ratio() -> None:
    ratio = fuzz.token_sort_ratio("測試test", "test測試")
    assert ratio == 1.0


def test_token_sort_ratio_preprocess() -> None:
    ratio = fuzz.token_sort_ratio("測試test", "test測試", preprocess=lambda x: x)
    assert ratio == 1.0


def test_token_sort_ratio_none() -> None:
    with pytest.raises(TypeError):
        fuzz.token_sort_ratio(None, None)


def test_token_sort_ratio_tokenizer() -> None:
    with pytest.raises(TypeError):
        fuzz.token_sort_ratio("測試test", "test測試", tokenizer=None)
