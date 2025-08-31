import random

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
