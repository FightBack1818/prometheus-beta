import pytest
from src.palindrome_pairs import palindrome_pairs

def test_basic_palindrome_pairs():
    # Test basic case with palindrome pairs
    words = ["bat", "tab", "cat"]
    result = palindrome_pairs(words)
    assert [0, 1] in result and [1, 0] in result

def test_empty_input():
    # Test with empty list
    words = []
    result = palindrome_pairs(words)
    assert result == []

def test_no_palindrome_pairs():
    # Test with no palindrome pairs
    words = ["hello", "world", "python"]
    result = palindrome_pairs(words)
    assert result == []

def test_single_word_palindrome():
    # Test where words have palindrome combinations
    words = ["a", "abc", "aba", ""]
    result = palindrome_pairs(words)
    # Check various palindrome combinations
    assert [2, 3] in result
    assert [3, 2] in result

def test_complex_palindrome_pairs():
    # More complex test case
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = palindrome_pairs(words)
    expected_pairs = [[0, 1], [1, 0], [3, 2], [2, 3]]
    
    # Check that all expected pairs are in the result
    for pair in expected_pairs:
        assert pair in result