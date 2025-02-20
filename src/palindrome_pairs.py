def palindrome_pairs(words):
    """
    Find indices of pairs of words that form palindromes when concatenated.
    
    Args:
        words (list): A list of strings
    
    Returns:
        list: A list of pairs of indices where concatenated words form a palindrome
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    for i in range(n):
        for j in range(n):
            # Skip same index
            if i == j:
                continue
            
            # Concatenate words in both orders
            concat1 = words[i] + words[j]
            concat2 = words[j] + words[i]
            
            # Check if either concatenation forms a palindrome
            if is_palindrome(concat1):
                result.append([i, j])
    
    return result