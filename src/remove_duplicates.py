def remove_duplicates(arr):
    """
    Remove duplicate elements from an array of integers with O(n) time complexity.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: A new list with duplicate elements removed, preserving original order
    """
    # Use a set to track seen elements for O(1) lookup
    seen = set()
    unique_list = []
    
    for num in arr:
        # Only add to unique_list if not seen before
        if num not in seen:
            seen.add(num)
            unique_list.append(num)
    
    return unique_list