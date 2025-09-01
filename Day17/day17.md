

**Tribonacci Sequence**
=======================

**Challenge Description**
------------------------

The Tribonacci sequence is a series of numbers where each number is the sum of the three preceding ones. When starting with 0, 0 and 1, the first 10 numbers in the sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.

**Task**
--------

Given an array containing the first three numbers of a Tribonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

**Functionality**
----------------

The `tribonacci_sequence` function takes two parameters:

* `start_sequence`: an array containing the first three numbers of the Tribonacci sequence
* `length`: an integer representing the length of the sequence

The function returns an array containing the Tribonacci sequence of the given length.

**Example Use Cases**
--------------------

* `tribonacci_sequence([0, 0, 1], 10)` returns `[0, 0, 1, 1, 2, 4, 7, 13, 24, 44]`
* `tribonacci_sequence([0, 1, 1], 5)` returns `[0, 1, 1, 2, 4]`
* `tribonacci_sequence([1, 1, 1], 0)` returns `[]`

**Code**
------

```python
def tribonacci_sequence(start_sequence, length):
    sequence = start_sequence[:]
    if length == 0:
        return []
    elif length == 1:
        return start_sequence[:1]
    elif length == 2:
        return start_sequence[:2]
    elif length == 3:
        return start_sequence
    else:
        while len(sequence) < length:
            total = sum(sequence[-3:])
            sequence.append(total)
    return sequence
```

**License**
-------

This code is licensed under the MIT License.

**Author**
-------

Akwo Makembe King "kingakwomakembe@gmail.com"