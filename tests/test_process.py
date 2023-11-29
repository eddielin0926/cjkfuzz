import pytest

from cjkfuzz import process


def test_process_extract():
    choices: list[str] = ["中文測試", "英文測試", "日文測驗", "韓文檢驗"]
    query = "中文測試"
    assert process.extract(query, choices, 2) == [(1.0, "中文測試"), (0.875, "英文測試")]


def test_process_extract_limit() -> None:
    with pytest.raises(ValueError):
        process.extract("中文測試", ["中文測試", "日本語テスト"], 0)
