import pytest

from cjkfuzz import process


def test_process_extract():
    choices = ["apple", "banana", "orange", "pear"]
    query = "banana"
    assert process.extract(query, choices, 2) == [(1.0, "banana"), (0.5833333333333334, "orange")]


def test_process_extract_limit() -> None:
    with pytest.raises(ValueError):
        process.extract("中文測試", ["中文測試", "日本語テスト"], 0)
