**Matrix Rotate**
================

A Python solution to the freeCodeCamp Daily Challenge: Matrix Rotate

**Challenge Description**
-------------------------

Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and return it.

**Solution**
------------

The solution is implemented in the `rotate` function, which takes a matrix as input and returns the rotated matrix.

**Example Use Cases**
--------------------

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated = rotate(matrix)
print(rotated)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

**Code**
------

```python
def rotate(matrix):
    n = len(matrix)
    m = len(matrix[0])
    transposed = []

    for i in range(m):
        new_row = []
        for j in range(n):
            new_row.append(matrix[j][i])
        transposed.append(new_row)

    for row in transposed:
        row.reverse()

    return transposed
```

**Explanation**
-------------

The `rotate` function first transposes the input matrix, and then reverses each row to achieve the rotation effect.

**License**
-------

This code is licensed under the MIT License.

**Author**
-------

Akwo Makembe King "kingakwomakembe@gmail.com"