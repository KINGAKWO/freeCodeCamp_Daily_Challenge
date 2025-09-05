IPv4 Validator
================

A Python solution to the freeCodeCamp Daily Challenge: IPv4 Validator

**Challenge Description**
-------------------------

Given a string, determine if it is a valid IPv4 Address. A valid IPv4 address consists of four integer numbers separated by dots (.). Each number must satisfy the following conditions:

* It is between 0 and 255 inclusive.
* It does not have leading zeros (e.g. 0 is allowed, 01 is not).
* Only numeric characters are allowed.

**Solution**
------------

The solution is implemented in the `is_valid_ipv4` function, which takes a string representing the IPv4 address as input and returns a boolean indicating whether the address is valid or not.

**Example Use Cases**
--------------------

```python
print(is_valid_ipv4("192.168.1.1"))  # True
print(is_valid_ipv4("0.0.0.0"))  # True
print(is_valid_ipv4("255.01.50.111"))  # False
print(is_valid_ipv4("255.00.50.111"))  # False
print(is_valid_ipv4("256.101.50.115"))  # False
print(is_valid_ipv4("192.168.101."))  # False
print(is_valid_ipv4("192168145213"))  # False
```

**Code**
------

```python
def is_valid_ipv4(ipv4):
    integer_numbers = ipv4.split(".")
    valid_address = []

    if len(integer_numbers) != 4:
        return False

    for i in integer_numbers:
        if i.isdigit():
            if len(i) > 1 and i[0]=="0":
                return False
            num = int(i)
            if 0 <= num <= 255:
                valid_address.append(num)
            else:
                return False
        else:
            return False
    return True
```

**License**
-------

This code is licensed under the MIT License.

**Author**
-------

Akwo Makembe King "kingakwomakembe@gmail.com"