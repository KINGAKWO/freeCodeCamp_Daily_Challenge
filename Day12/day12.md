# Day 12: Unorder of Operations
==========================

## Challenge Description
------------------------

Given an array of integers and an array of string operators, apply the operations to the numbers sequentially from left-to-right. Repeat the operations as needed until all numbers are used. Return the final result.

## Example Use Cases
--------------------

* Input: `[1, 2, 3, 4, 5]` and `['+', '*']`
* Output: `1 + 2 * 3 + 4 * 5` (ignoring standard order of operations)

## Solution
------------

The solution is implemented in the `evaluate` function, which takes two arrays as input: `numbers` and `operators`.

## Explanation
-------------

The `evaluate` function iterates over the `operators` array and applies each operation to the corresponding numbers in the `numbers` array. The result is then used as the input for the next operation.

## License
-------

This code is licensed under the MIT License.

## Author
-------

AKWO MAKEMBE KING kingakwomakembe@gmail.com