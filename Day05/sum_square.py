<<<<<<< HEAD
def sum_of_squares(n):
    if n<1 or n>1000:
        print("invalid output")
        raise ValueError("Input must be between 1 and 1000")
        return 0
    result = 0
    for num in range(1, n+1):
        result += num**2
        print(result)
    return result

sum_of_squares(5)
=======
def sum_of_squares(n):
    if n<1 or n>1000:
        print("invalid output")
        raise ValueError("Input must be between 1 and 1000")
        return 0
    result = 0
    for num in range(1, n+1):
        result += num**2
        print(result)
    return result

sum_of_squares(5)
>>>>>>> ec33a251652659f92073ba3ed7671739354a1f88
sum_of_squares(1001)