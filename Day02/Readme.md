**Anagram Detector**
=====================

A Python solution to the freeCodeCamp Daily Challenge: Anagram Detector

**Challenge Description**
-------------------------

Given two strings, determine if they are anagrams of each other (contain the same characters in any order). Ignore casing and white space.

**Solution**
------------

The solution is implemented in the `are_anagrams` function, which takes two strings as input and returns `True` if they are anagrams, and `False` otherwise.

**Example Use Cases**
--------------------

```python
are_anagrams("listen", "silent")  # True
are_anagrams("Hello", "World")  # False
```

**Code**
------

```python
def are_anagrams(str1, str2):
    str1 = str1.replace(" ","")
    str2 = str2.replace(" ","")
    str1 = sorted(str1.lower().strip())
    str2 = sorted(str2.lower().strip())
    if  str1 == str2:
        print('it is an anagram')
        return True
    else:
        print("Not an anagram")
```

**License**
-------

This code is licensed under the MIT License.

**Author**
-------
Akwo Makembe King "kingakwomakembe@gmail.com"


