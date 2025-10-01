def to_decimal(binary_str):
    """
    Convert a binary string to its decimal equivalent.

    Args:
        binary_str (str): A string of binary digits (e.g., "1010").

    Returns:
        int: Decimal representation of the binary string.
    """
    digits = list(binary_str)[::-1]  # Reverse to start from rightmost digit
    decimal = 0
    power = 0

    for digit in digits:
        decimal += int(digit) * (2 ** power)
        power += 1

    return decimal
