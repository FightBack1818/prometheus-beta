import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    input_arr = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_arr) == expected

def test_remove_duplicates_empty_list():
    """Test with an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test with a list that has no duplicates"""
    input_arr = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_arr) == input_arr

def test_remove_duplicates_all_duplicates():
    """Test with a list of all duplicate elements"""
    input_arr = [2, 2, 2, 2, 2]
    assert remove_duplicates(input_arr) == [2]

def test_remove_duplicates_mixed_types():
    """Test with repeated elements of different order"""
    input_arr = [5, 3, 1, 5, 3, 2, 1]
    expected = [5, 3, 1, 2]
    assert remove_duplicates(input_arr) == expected