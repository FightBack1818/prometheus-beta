import pytest
from src.near_palindrome_pairs import find_near_palindrome_pairs

def test_near_palindrome_pairs_basic():
    # Basic test case with near palindromes
    input_strings = ["abc", "cba", "abca", "deified"]
    result = find_near_palindrome_pairs(input_strings)
    assert len(result) > 0, "Should find near palindrome pairs"
    
def test_near_palindrome_pairs_empty():
    # Test with empty input
    assert find_near_palindrome_pairs([]) == [], "Should return empty list for empty input"
    
def test_near_palindrome_pairs_single_string():
    # Test with single string input
    assert find_near_palindrome_pairs(["abc"]) == [], "Should return empty list for single string"
    
def test_near_palindrome_pairs_no_near_palindromes():
    # Test with strings that are not near palindromes
    input_strings = ["hello", "world", "python"]
    result = find_near_palindrome_pairs(input_strings)
    assert len(result) == 0, "Should return empty list when no near palindromes exist"
    
def test_near_palindrome_pairs_edge_cases():
    # Test various edge cases
    test_cases = [
        (["racecar", "radar", "level"], True),  # Palindromes included
        (["abc", "cab", "acb"], True),  # Strings close to palindromes
        (["a", "b", "c"], False),  # Very short strings
        (["", ""], False)  # Empty strings
    ]
    
    for input_strings, expected_result in test_cases:
        result = find_near_palindrome_pairs(input_strings)
        if expected_result:
            assert len(result) > 0, f"Should find near palindrome pairs in {input_strings}"
        else:
            assert len(result) == 0, f"Should not find near palindrome pairs in {input_strings}"