import pytest

from cjkfuzz import fuzz


def test_fuzz_ratio() -> None:
    ratio = fuzz.ratio("中文測試", "中文測試")
    assert ratio == 1.0


def test_fuzz_ratio_pinyin() -> None:
    ratio = fuzz.ratio("你好", "妳好")
    assert ratio == 1.0


def test_fuzz_ratio_preprocess() -> None:
    ratio = fuzz.ratio("中文測試", "中文測試")
    assert ratio == 1.0


def test_fuzz_ratio_none() -> None:
    with pytest.raises(TypeError):
        fuzz.ratio(None, None)


def test_fuzz_partial_ratio() -> None:
    ratio = fuzz.partial_ratio("test", "more tests")
    assert ratio == 1.0


def test_fuzz_partial_ratio_preprocess() -> None:
    ratio = fuzz.partial_ratio("more tests", "test")
    assert ratio == 1.0


def test_fuzz_partial_ratio_none() -> None:
    with pytest.raises(TypeError):
        fuzz.partial_ratio(None, None)
