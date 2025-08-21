**Sum of Squares**
================

A Python solution to calculate the sum of squares of integers from 1 to a given number.

**Challenge Description**
-------------------------

Given a positive integer up to 1,000, return the sum of all the integers squared from 1 up to the number.

**Solution**
------------

The solution is implemented in the `sum_of_squares` function, which takes an integer `n` as input and returns the sum of squares of integers from 1 to `n`.

**Example Use Cases**
--------------------

```python
print(sum_of_squares(5))  # Output: 55
print(sum_of_squares(1001))  # Output: 332833500
```

**Code**
------

```python
def sum_of_squares(n):
    if n < 1 or n > 1000:
        print("Invalid input")
        raise ValueError("Input must be between 1 and 1000")
    result = 0
    for num in range(1, n + 1):
        result += num ** 2
    return result
```

**Explanation**
-------------

The `sum_of_squares` function takes an integer `n` as input and checks if it is within the valid range of 1 to 1000. If the input is invalid, it raises a `ValueError`.

The function then initializes a variable `result` to 0 and uses a `for` loop to iterate from 1 to `n`. In each iteration, it calculates the square of the current number and adds it to the `result`.

Finally, the function returns the `result`, which is the sum of squares of integers from 1 to `n`.

**License**
-------

This code is licensed under the MIT License.

**Author**
-------
Akwo Makembe King  kingakwomakembe@gmail.com
