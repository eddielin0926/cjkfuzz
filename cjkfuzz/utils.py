"""Provides utility functions for cjkfuzz."""

ranges = [
    {"from": ord("\u3300"), "to": ord("\u33ff")},  # compatibility ideographs
    {"from": ord("\ufe30"), "to": ord("\ufe4f")},  # compatibility ideographs
    {"from": ord("\uf900"), "to": ord("\ufaff")},  # compatibility ideographs
    {"from": ord("\U0002f800"), "to": ord("\U0002fa1f")},  # compatibility ideographs
    {"from": ord("\u3040"), "to": ord("\u309f")},  # Japanese Hiragana
    {"from": ord("\u30a0"), "to": ord("\u30ff")},  # Japanese Katakana
    {"from": ord("\u2e80"), "to": ord("\u2eff")},  # cjk radicals supplement
    {"from": ord("\u4e00"), "to": ord("\u9fff")},
    {"from": ord("\u3400"), "to": ord("\u4dbf")},
    {"from": ord("\U00020000"), "to": ord("\U0002a6df")},
    {"from": ord("\U0002a700"), "to": ord("\U0002b73f")},
    {"from": ord("\U0002b740"), "to": ord("\U0002b81f")},
    {"from": ord("\U0002b820"), "to": ord("\U0002ceaf")},  # included as of Unicode 8.0
]


def is_cjk_char(char: str) -> bool:
    return any([range["from"] <= ord(char) <= range["to"] for range in ranges])
