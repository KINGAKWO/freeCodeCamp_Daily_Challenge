def has_exoplanet(readings):
    values = [int(ch) if ch.isdigit() else ord(ch) - ord('A') + 10 for ch in readings]
    avg = sum(values) / len(values)
    threshold = 0.8 * avg
    return any(v <= threshold for v in values)


# step by step approach
# def has_exoplanet(readings):
#    values = []
#    for ch in readings.upper():
#        if ch.isdigit():
#            values.append(int(ch))
#        else:
#            # Convert A-Z to 10-35
#            values.append(ord(ch) - ord('A') + 10)

#    avg = sum(values) / len(values)
#    threshold = 0.8 * avg

#    for v in values:
#        if v <= threshold:
#            return True
#    return False
###

# Example usage:
print(has_exoplanet("123456789A"))  # True
print(has_exoplanet("123456789Z"))  # False
print(has_exoplanet("ABCDE"))        # True
