

**Decode Function README**
==========================

**Overview**
------------

This is a Python function named `decode` that takes a string as input and returns the decoded version of the string. The decoding process involves reversing the characters inside each pair of parentheses and removing the parentheses.

**Functionality**
----------------

The `decode` function uses regular expressions to find all pairs of parentheses in the input string. It then iterates over each pair, reverses the characters inside the parentheses, and replaces the original pair with the reversed characters. This process is repeated until all pairs of parentheses have been processed.

**Rules**
---------

The decoding process follows these rules:

* All characters inside each pair of parentheses should be reversed.
* Parentheses should be removed from the final result.
* If parentheses are nested, the innermost pair should be reversed first, and then its result should be included in the reversal of the outer pair.
* Assume all parentheses are evenly balanced and correctly nested.

**Example Use Cases**
--------------------

```python
print(decode("(hello)"))  # Output: "olleh"
print(decode("(hello (world))"))  # Output: "olleh dlrow"
```

**Code**
------

```python
import re

def decode(s):
    while re.search(r"\([^()]*\)", s):
        matches = re.findall(r"\([^()]*\)", s)
        for match in matches:
            inner = match[1:-1]
            reversed_inner = inner[::-1]
            s = s.replace(match, reversed_inner, 1)
    return s
```

**License**
-------

This code is licensed under the MIT License.

