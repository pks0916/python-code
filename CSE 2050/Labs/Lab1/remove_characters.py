def remove_characters(input_string, to_remove):
    """removes any char that in input string and also in to remove"""
    new_string = ''
    for char in input_string:
        if char not in to_remove:
            new_string += char
    return new_string
            