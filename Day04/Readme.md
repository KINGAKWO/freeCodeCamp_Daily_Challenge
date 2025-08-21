

**Factorial Calculator**
=====================

A Python solution to calculate the factorial of a given integer.

**Challenge Description**
-------------------------

Given an integer from zero to 20, return the factorial of that number. The factorial of a number is the product of all the numbers between 1 and the given number.

**Solution**
------------

The solution is implemented in the `factorial` function, which takes an integer `n` as input and returns the factorial of `n`.

**Example Use Cases**
--------------------

```python
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
```

**Code**
------

```python
def factorial(n):
    if not isinstance(n, int):
        return "Please enter an integer"
    if n < 0 or n > 20:
        return "Give an integer from 0 to 20"
    
    result = 1  # accumulator
    for i in range(1, n + 1):
        result *= i  # multiply progressively
    return result
```

**Explanation**
-------------

The `factorial` function takes an integer `n` as input and checks if it is a valid integer and within the range of 0 to 20. If the input is invalid, it returns an error message.

The function then initializes a variable `result` to 1 and uses a `for` loop to iterate from 1 to `n`. In each iteration, it multiplies the current number with the `result` and updates the `result`.

Finally, the function returns the `result`, which is the factorial of `n`.

**License**
-------

This code is licensed under the MIT License.

**Author**
-------
Akwo Makembe King  kingakwomakembe@gmail.com
