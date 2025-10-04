import re


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1

    if re.search(r'\d', password):
        score += 1

    if re.search(r'[!@#$%^&*]', password):
        score += 1

    if score == 4:
        return "strong"
    elif score >= 2:
        return "medium"
    else:
        return "weak"


# Example usage:
password = input("Enter a password to check its strength: ")
print("Password strength:", check_strength(password))
