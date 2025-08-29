# freeCodeCamp Daily Challenge: Day 14
=====================================

## Candlelight Problem
--------------------

Given an integer representing the number of candles you start with, and an integer representing how many burned candles it takes to create a new one, return the number of candles you will have used after creating and burning as many as you can.

### Example
--------

* Input: `candles = 7`, `makeNew = 2`
* Output: `13`

### Explanation
-------------

The function `burn_candles` takes two parameters: `candles` and `makeNew`. It simulates the process of burning candles and creating new ones until no more candles can be created.

### Code
------

```python
def burn_candles(candles, makeNew):
    total_burned = 0
    leftovers = 0

    while candles > 0:
        # Burn current candles
        total_burned += candles
        leftovers += candles
        candles = 0

        # Recycle leftovers into new candles
        new_candles = leftovers // makeNew
        leftovers = leftovers % makeNew
        candles += new_candles

    return total_burned
```

### Usage
-----

```python
print(burn_candles(7, 2))  # Output: 13
```

### License
-------

This code is licensed under the MIT License.

### Author
-------

Akwo Makembe King "kingakwomakembe@gmail.com"