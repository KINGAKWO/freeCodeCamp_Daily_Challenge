def second_largest(arr):
    """
    Return the second largest distinct number in the array.

    Args:
        arr (list): List of numbers (ints or floats).

    Returns:
        int | float: The second largest distinct number.
    """
    sorted_num = sorted(set(arr), reverse=True)
    print(sorted_num)

    if len(sorted_num) < 2:
        raise ValueError("Array must contain at least two distinct numbers.")
    return sorted_num[1]


# Test cases
try:
    print(second_largest([1, 2, 3, 4, 5]))  # Output: 4
    print(second_largest([10, -17, 55.5, 44, 91]))  # Output: 55.5
    print(second_largest([2, 3, 4, 6, 6]))  # Output: 4
    print(second_largest([5]))  # Should raise ValueError
except ValueError as e:
    print(e)
