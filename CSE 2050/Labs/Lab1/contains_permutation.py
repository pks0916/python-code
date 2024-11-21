def contains_permutation(input_string, pattern):
    pattern_length = len(pattern)

    """Iterate through each possible substring of length 'pattern_length' in input_string"""
    for i in range(len(input_string) - pattern_length + 1):
        substring = input_string[i:i + pattern_length]

        """ Check if the set of characters in the substring is equal to the set of characters in the pattern"""
        if set(substring) == set(pattern):
            return True

    """ if no match return false"""
    return False