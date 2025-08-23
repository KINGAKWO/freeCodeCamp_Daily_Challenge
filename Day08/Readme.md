**Unnatural Prime**
================

A Python solution to determine if a number is a prime or a negative prime.

**Challenge Description**
-------------------------

Given an integer, determine if it is a prime or a negative prime.

**What is an Unnatural Prime?**
-----------------------------

A prime is a positive integer > 1 divisible only by 1 and itself.
A negative prime is simply the negative version of a prime.
(And no, 0 and 1 don’t make the cut.)

**Solution**
------------

The solution is implemented in the `is_unnatural_prime` function, which takes an integer as input and returns `True` if it is a prime or negative prime, and `False` otherwise.

**Example Use Cases**
--------------------

```python
print(is_unnatural_prime(5))  # True
print(is_unnatural_prime(-5))  # True
print(is_unnatural_prime(4))  # False
```

**Code**
------

```python
def is_unnatural_prime(num):
    if abs(num) <= 1:
        return False
    n = abs(num)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

**Explanation**
-------------

The `is_unnatural_prime` function uses the absolute value of the input number to check for primality, then returns `True` if the number is prime or negative prime, and `False` otherwise.

**License**
-------

This code is licensed under the MIT License.

**Author**
-------

Akwo Makembe King "kingakwomakembe@gmail.com"