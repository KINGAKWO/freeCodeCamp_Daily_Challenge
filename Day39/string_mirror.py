def is_mirror(str1, str2):
    """
    Determines if the second string is a mirror of the first.
    
    A mirror means the second string contains the same alphabetical characters
    as the first string, but in reverse order. Case-sensitive. Non-alphabetical
    characters are ignored.

    Args:
        str1 (str): The original string.
        str2 (str): The string to compare as a potential mirror.

    Returns:
        bool: True if str2 is a mirror of str1, False otherwise.
    """
    # Filter out non-alphabetical characters
    filtered1 = ''.join(char for char in str1 if char.isalpha())
    filtered2 = ''.join(char for char in str2 if char.isalpha())

    # Compare filtered1 with the reverse of filtered2
    return filtered1 == filtered2[::-1]