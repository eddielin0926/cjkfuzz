from cjkfuzz import process


def test_process_extract() -> None:
    query = "中文測試"
    choices = ["中文測試", "英文測試"]
    extracted = process.extract(query, choices)
    assert extracted == [("中文測試", 0)]
