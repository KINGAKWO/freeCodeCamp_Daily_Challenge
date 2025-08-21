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
sum_of_squares(1001)