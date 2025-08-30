# Array Duplicates
================

A Python solution to the freeCodeCamp Daily Challenge: Array Duplicates

## Challenge Description
-------------------------

Given an array of integers, return an array of integers that appear more than once in the initial array, sorted in ascending order. If no values appear more than once, return an empty array.

## Solution
------------

The solution is implemented in the `find_duplicates` function, which takes an array of integers as input and returns an array of integers that appear more than once in the initial array, sorted in ascending order.

### Code
------

```python
def find_duplicates(arr):
    seen = set()
    duplicates = []
     
    for num in arr:
         if num in seen:
             if num not in duplicates:
                duplicates.append(num)
             
 
         else:
             seen.add(num)
    print(duplicates)
    return sorted(duplicates)
```

### Example Use Cases
--------------------

```python
print(find_duplicates([1, 2, 3, 4, 5]))  # Output: []
print(find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]))  # Output: [-6, 0, 2, 3, 4, 5, 23]
```

### License
-------

This code is licensed under the MIT License.

### Author
-------

Akwo Makembe King "kingakwomakembe@gmail.com"

### Date
-------

2023-07-15