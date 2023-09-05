from cjkfuzz import tokenizer


def test_tokenizer() -> None:
    tokens = tokenizer.default("中文測試Chinese Test")
    assert tokens == ["中", "文", "測", "試", "Chinese", "Test"]
