# Unique Characters
================

A Python solution to the freeCodeCamp Daily Challenge: Unique Characters

## Challenge Description
-------------------------

Given a string, determine if all the characters in the string are unique.

* Uppercase and lowercase letters should be considered different characters.

## Solution
------------

The solution is implemented in the `all_unique` function, which takes a string as input and returns `True` if all characters are unique, and `False` otherwise.

## Example Use Cases
--------------------

```python
print(all_unique("abc"))  # True
print(all_unique("aA"))  # True
print(all_unique("QwErTy123!@"))  # True
print(all_unique("~!@#$%^&*()_+"))  # True
print(all_unique("hello"))  # False
print(all_unique("freeCodeCamp"))  # False
print(all_unique("!@#*$%^&*()aA"))  # False
```

## Code
------

```python
def all_unique(s):
    char = list(s)
    unique = set(s)
    if len(char) == len(unique):
        return True
    else:
        return False
```

## Explanation
-------------

The `all_unique` function works by converting the input string to a list of characters and a set of unique characters. If the lengths of the two are equal, it means all characters are unique, and the function returns `True`. Otherwise, it returns `False`.

## License
-------

This code is licensed under the MIT License.

## Author
-------

Akwo Makembe King "kingakwomakembe@gmail.com"