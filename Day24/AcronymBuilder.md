**Acronym Builder**
================

A Python solution to the freeCodeCamp Daily Challenge: Acronym Builder

**Challenge Description**
------------------------

Given a string containing one or more words, return an acronym of the words using the following constraints:

* The acronym should consist of the first letter of each word capitalized, unless otherwise noted.
* The acronym should ignore the first letter of these words unless they are the first word of the given string: a, for, an, and, by, and of.
* The acronym letters should be returned in order they are given.
* The acronym should not contain any spaces.

**Solution**
------------

The solution is implemented in the `build_acronym` function, which takes a string as input and returns the acronym.

**Example Use Cases**
--------------------

```python
print(build_acronym("Search Engine Optimization"))  # "SEO"
print(build_acronym("Frequently Asked Questions"))  # "FAQ"
print(build_acronym("National Aeronautics and Space Administration"))  # "NASA"
print(build_acronym("Federal Bureau of Investigation"))  # "FBI"
print(build_acronym("For your information"))  # "FYI"
print(build_acronym("By the way"))  # "BTW"
print(build_acronym("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily"))  # "AUHWPOTIMSH"
```

**Code**
------

```python
def build_acronym(s):
    word = s.split(" ")
    ignore = ['a', "for", "an", "and", "by", "of"]
    acronym = []

    for idx, i in enumerate(word):
        if i.lower() in ignore and idx != 0:
            continue
        else:
            acronym.append(i[0])
    return "".join(acronym).upper()
```

**License**
-------

This code is licensed under the MIT License.

**Author**
-------

Akwo Makembe King [kingakwomakembe@gmail.com](mailto:kingakwomakembe@gmail.com)