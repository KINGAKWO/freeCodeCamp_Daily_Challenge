# Roman Numeral Parser
======================

A Python solution to the freeCodeCamp Daily Challenge: Roman Numeral Parser

## Challenge Description
------------------------

Given a string representing a Roman numeral, return its integer value.

Roman numerals consist of the following symbols and values:

| Symbol | Value |
| --- | --- |
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Numerals are read left to right. If a smaller numeral appears before a larger one, the value is subtracted. Otherwise, values are added.

## Solution
------------

The solution is implemented in the [parse_roman_numeral](freeCodeCamp_Daily_Challenge\Day23\roman_Numeral_Parser.py) function, which takes a string representing the Roman numeral as input and returns its integer value.

## Example Use Cases
--------------------

```python
print(parse_roman_numeral("III"))  # 3
print(parse_roman_numeral("IV"))  # 4
print(parse_roman_numeral("XXVI"))  # 26
print(parse_roman_numeral("XCIX"))  # 99
print(parse_roman_numeral("CDLX"))  # 460
print(parse_roman_numeral("DIV"))  # 504
print(parse_roman_numeral("MMXXV"))  # 2025



License
This code is licensed under the MIT License.

Author
Akwo Makembe King kingakwomakembe@gmail.com