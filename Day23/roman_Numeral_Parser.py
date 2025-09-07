def parse_roman_numeral(roman):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    max_seen = 0  

    # Traverse from right to left
    for char in reversed(roman):
        value = values[char]
        if value >= max_seen:
            total += value
            max_seen = value
        else:
            total -= value

    return total
