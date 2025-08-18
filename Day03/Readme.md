**Targeted Sum**
================

A Python solution to the freeCodeCamp Daily Challenge: Targeted Sum

**Challenge Description**
-------------------------

Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value.

Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.

The returned array should have the indices in ascending order.

**Solution**
------------

The solution is implemented in the `find_target` function, which takes an array of numbers and an integer target as input and returns the indices of the two numbers that add up to the target value.

**Example Use Cases**
--------------------

```python
arr = [2, 7, 11, 15]
target = 9
print(find_target(arr, target))  # Output: [0, 1]

arr = [3, 5, 8, 10]
target = 12
print(find_target(arr, target))  # Output: [1, 3]

arr = [1, 2, 3, 4]
target = 10
print(find_target(arr, target))  # Output: "Target not found"
```

**Code**
------

```python
def find_target(arr, target):
    for i in range(len(arr)-1):
        if i < len(arr)-1:
            for j in range(i + 1, len(arr)): 
                if j<len(arr):
                    sum = arr[i] + arr[j]
                    if sum == target:
                        return [i,j]
    return "Target not found"
```

**License**
-------

This code is licensed under the MIT License.

**Author**
-------
Akwo Makembe King "kingakwomakembe@gmail.com"
