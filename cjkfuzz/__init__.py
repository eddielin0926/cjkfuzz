"""CJK Fuzzy Matching Library

This library provides fuzzy matching algorithms for CJK (Chinese, Japanese, Korean) strings.
"""
from cjkfuzz import fuzz, hamming, jaro, jaro_winkler, levenshtein

__author__: str = "Eddie Lin"
__license__: str = "MIT"
__version__ = "0.0.3"

__all__ = ["fuzz", "hamming", "jaro", "jaro_winkler", "levenshtein"]
