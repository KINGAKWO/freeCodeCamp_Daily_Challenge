def is_unnatural_prime(num):
    if abs(num) <= 1:
        return False
    n = abs(num)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True