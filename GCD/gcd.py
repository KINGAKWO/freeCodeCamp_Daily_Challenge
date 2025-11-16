def gcd(a, b):
    # Handling zeros
    if a == 0 and b == 0:
        return 0  
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)

    # Handling  negatives
    a, b = abs(a), abs(b)

    # Euclidean algorithm
    GCD = a if b == 0 else gcd(b, a % b)

    return GCD
