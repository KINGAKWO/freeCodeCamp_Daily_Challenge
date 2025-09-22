def digits_or_letters(s):
    """
    This function takes a string as input and returns "letters"
    if the string contains more letters than digits,
    "digits" if it contains more digits than letters, or "tie" if the counts
    """
    count_letters = 0
    count_digits = 0

    for char in s:
        if char.isalpha():
            count_letters += 1
        elif char.isdigit():
            count_digits += 1

    if count_letters > count_digits:
        return "letters"
    elif count_digits > count_letters:
        return "digits"
    else:
        return "tie"