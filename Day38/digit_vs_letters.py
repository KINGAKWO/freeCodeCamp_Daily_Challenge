def digits_or_letters(s: str) -> str:
    """
    Determine whether a string has more digits, more letters, or a tie.
    
    Digits: 0–9
    Letters: A–Z, a–z
    Any other characters are ignored.
    
    Args:
        s (str): The input string.
    
    Returns:
        str: "digits", "letters", or "tie"
    """
    count_letters = sum(1 for char in s if char.isalpha())
    count_digits = sum(1 for char in s if char.isdigit())

    if count_letters > count_digits:
        return "letters"
    elif count_digits > count_letters:
        return "digits"
    return "tie"
