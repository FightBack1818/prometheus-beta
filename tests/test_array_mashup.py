import pytest
from src.array_mashup import arrayMashup

def test_array_mashup_basic():
    """Test basic array mashup functionality"""
    assert arrayMashup([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

def test_array_mashup_single_element():
    """Test array mashup with single-element arrays"""
    assert arrayMashup([10], [20]) == [30]

def test_array_mashup_zeros():
    """Test array mashup with zero-like inputs"""
    assert arrayMashup([1, 0, 5], [0, 2, 3]) == [1, 2, 8]

def test_array_mashup_unequal_length():
    """Test that unequal length arrays raise a ValueError"""
    with pytest.raises(ValueError, match="Input arrays must have the same length"):
        arrayMashup([1, 2], [1, 2, 3])

def test_array_mashup_non_list_input():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Inputs must be lists"):
        arrayMashup("not a list", [1, 2, 3])

def test_array_mashup_non_integer_input():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError, match="All elements must be positive integers"):
        arrayMashup([1, 2, 'a'], [3, 4, 5])

def test_array_mashup_non_positive_input():
    """Test that non-positive inputs raise a TypeError"""
    with pytest.raises(TypeError, match="All elements must be positive integers"):
        arrayMashup([1, 2, -3], [3, 4, 5])