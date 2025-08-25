**camelCase Converter**
=====================

A Python solution to convert a given string to its camel case version.

**Challenge Description**
-------------------------

Given a string, return its camel case version using the following rules:

* Words in the string argument are separated by one or more characters from the following set: space ( ), dash (-), or underscore (_). Treat any sequence of these as a word break.
* The first word should be all lowercase.
* Each subsequent word should start with an uppercase letter, with the rest of it lowercase.
* All spaces and separators should be removed.

**Solution**
------------

The solution is implemented in the `to_camel_case` function, which takes a string as input and returns its camel case version.

**Example Use Cases**
--------------------

```python
print(to_camel_case("hello world"))  # "helloWorld"
print(to_camel_case("FREE cODE cAMP"))  # "freeCodeCamp"
print(to_camel_case("HELLO WORLD"))  # "helloWorld"
print(to_camel_case("secret agent-X"))  # "secretAgentX"
print(to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk"))  # "yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk"
```

**Code**
------

```python
import re

def to_camel_case(s):
    camel = []
    words = [w for w in re.split(r"[ _-]+", s.strip()) if w]
    for i, word in enumerate(words):
        if i == 0:
            first_word = word.lower()
            camel.append(first_word)
        else:
            first_letter = word[0].upper()
            others = word[1:].lower()
            camel.append(first_letter + others)
    return ''.join(camel)
```

**Explanation**
-------------

The `to_camel_case` function uses regular expressions to split the input string into words, and then iterates over the words to convert them to camel case. The first word is converted to lowercase, and subsequent words are converted to uppercase followed by lowercase.

**License**
-------

This code is licensed under the MIT License.

**Author**
-------

Akwo Makembe King kingakwomakembe@gmail.com
**Date**
2023-07-10
