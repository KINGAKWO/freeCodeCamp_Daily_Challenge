import math


def is_perfect_square(n):
    """ Determine whether an integer is a perfect square.
    A number is a perfect square if there exists an integer m
    such that m * m == n.

    Args: n (int): The integer to test.

    Returns: bool: True if n is a perfect square (including 0),
    False otherwise. """
    if n < 0:
        return False
    root = math.isqrt(n)
    return root * root == n


