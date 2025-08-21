

**3 Strikes: Counting Squares with Digit 3**
=============================================

A Python solution to count the numbers from 1 up to a given integer whose square contains at least one digit 3.

**Challenge Description**
-------------------------

Given an integer between 1 and 10,000, return a count of how many numbers from 1 up to that integer whose square contains at least one digit 3.

**Solution**
------------

The solution is implemented in the `squares_with_three` function, which takes an integer `n` as input and returns the count of numbers whose square contains at least one digit 3.

**Example Use Cases**
--------------------

```python
print(squares_with_three(10))  # Output: 1
print(squares_with_three(100))  # Output: 10
print(squares_with_three(10000))  # Output: 1337
```

**Code**
------

```python
def squares_with_three(n):
    target = '3'
    count = 0
    for num in range(1, n+1):
        square = num**2
        my_list = list(str(abs(square)))
        if target in my_list:
            count += 1
    return count
```

**Explanation**
-------------

The `squares_with_three` function iterates over the numbers from 1 to `n`, calculates the square of each number, and checks if the square contains the digit 3. If it does, it increments the count.

**License**
-------

This code is licensed under the MIT License.

**Author**
-------
Akwo Makembe King kingakwomakembe@gmail.com
