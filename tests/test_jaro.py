import pytest

from cjkfuzz import jaro


def test_jaro_similarity() -> None:
    similarity = jaro.similarity("This is an arbitrary sentence", "It is an random string")
    assert similarity == pytest.approx(0.6138322884012539)


def test_jaro_similarity_same() -> None:
    similarity = jaro.similarity("中文測試", "中文測試")
    assert similarity == 1.0


def test_jaro_similarity_no_common() -> None:
    similarity = jaro.similarity("中文測試", "日本語テスト")
    assert similarity == 0.0


def test_jaro_similarity_invalid() -> None:
    with pytest.raises(ValueError):
        jaro.similarity("", "")
