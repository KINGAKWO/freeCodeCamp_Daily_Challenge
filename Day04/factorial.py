def factorial(n):
    if not isinstance(n, int):
        return "Please enter an integer"
    if n < 0 or n > 20:
        return "Give an integer from 0 to 20"
    
    result = 1  # accumulator
    for i in range(1, n + 1):
        result *= i  # multiply progressively
    return result
