def arrayMashup(array1, array2):
    """
    Mash up two arrays by summing elements at corresponding indices.
    
    Args:
        array1 (list): First list of positive integers
        array2 (list): Second list of positive integers
    
    Returns:
        list: A new list where each element is the sum of elements at corresponding indices
    
    Raises:
        ValueError: If input arrays have different lengths
        TypeError: If inputs are not lists or contain non-integer elements
    """
    # Validate input types
    if not (isinstance(array1, list) and isinstance(array2, list)):
        raise TypeError("Inputs must be lists")
    
    # Validate input lengths
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have the same length")
    
    # Validate all elements are positive integers
    if not (all(isinstance(x, int) and x > 0 for x in array1) and 
            all(isinstance(x, int) and x > 0 for x in array2)):
        raise TypeError("All elements must be positive integers")
    
    # Perform array mashup
    return [a + b for a, b in zip(array1, array2)]