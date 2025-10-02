def to_binary(decimal):
    """
    Convert a non-negative integer to its binary representation as a string.

    Args:
        decimal (int): A non-negative integer.

    Returns:
        str: Binary representation of the input integer.
    """
    return bin(decimal)[2:]