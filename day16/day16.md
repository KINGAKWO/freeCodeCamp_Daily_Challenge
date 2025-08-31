**Hex Generator**
================

A Python solution to the freeCodeCamp Daily Challenge: Hex Generator

**Challenge Description**
-------------------------

Given a named CSS color string, generate a random hexadecimal (hex) color code that is dominant in the given color.

**Solution**
------------

The solution is implemented in the `generate_hex` function, which takes a string representing the color as input and returns a random six-character hex color code.

**Example Use Cases**
--------------------

```python
print(generate_hex("red"))  # "FF0000"
print(generate_hex("green"))  # "00FF00"
print(generate_hex("blue"))  # "0000FF"
print(generate_hex("yellow"))  # "Invalid color"
```

**Code**
------

```python
def generate_hex(color):
    valid_colors = ["red", "green", "blue"]
    if color not in valid_colors:
        return "Invalid color"
    
    r, g, b = 0, 0, 0

    dominant = random.randint(200, 255)   # strong intensity
    secondary1 = random.randint(0, 150)   # weaker
    secondary2 = random.randint(0, 150)

    if color == "red":
        r, g, b = dominant, secondary1, secondary2
    elif color == "green":
        r, g, b = secondary1, dominant, secondary2
    elif color == "blue":
        r, g, b = secondary1, secondary2, dominant

    return f"{r:02X}{g:02X}{b:02X}"
```

**Explanation**
-------------

The `generate_hex` function uses a simple and efficient approach to generate a random hex color code. It first checks if the input color is valid, and if not, returns "Invalid color". Then, it generates three random numbers representing the intensity of the red, green, and blue components of the color. The dominant component is set to a strong intensity, while the other two components are set to weaker intensities. Finally, the function returns a six-character hex color code representing the generated color.

**License**
-------

This code is licensed under the MIT License.

**Author**
-------

Akwo Makembe King "kingakwomakembe@gmail.com"