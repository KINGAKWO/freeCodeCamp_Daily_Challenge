import re


def format_number(s):
    """
    Formats a phone number string into the format:
    +{country code} ({area code}) {exchange code}-{line number}
    """
    number = re.fullmatch(r"(\d)(\d{3})(\d{3})(\d{4})", s)
    if not number:
        raise ValueError("Input must be exactly 10 digits")
    return f"+{number.group(1)} ({number.group(2)}) {number.group(3)}-{number.group(4)}"


format_number("05552340182")
