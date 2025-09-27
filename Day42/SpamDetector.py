import re


def is_spam(phone):
    """
    Determines if a phone number is spam
    based on formatting and digit patterns.


    Format: "+A (BBB) CCC-DDDD"
    - A: Country code (any length)
    - BBB: Area code (3 digits)
    - CCC-DDDD: Local number (3 + 4 digits)

    Spam criteria:
    1. Country code is >2 digits or doesn't start with '0'
    2. Area code is >900 or <200
    3. Sum of CCC digits appears in DDDD
    4. Any digit repeats 4+ times in a row (ignoring formatting)

    Returns:
        bool: True if spam, False otherwise
    """

    # Extract digits using regex
    match = re.match(r"\+(\d+)\s\((\d{3})\)\s(\d{3})-(\d{4})", phone)
    if not match:
        raise ValueError("Invalid phone format")

    country, area, ccc, dddd = match.groups()

    # Check 1: Country code
    if len(country) > 2 or not country.startswith("0"):
        return True

    # Check 2: Area code range
    area_int = int(area)
    if area_int > 900 or area_int < 200:
        return True

    # Check 3: Sum of CCC digits appears in DDDD
    sum_ccc = sum(int(d) for d in ccc)
    if str(sum_ccc) in dddd:
        return True

    # Check 4: Repeated digit 4+ times in a row
    digits_only = re.sub(r"\D", "", phone)
    for i in range(len(digits_only) - 3):
        if digits_only[i] * 4 == digits_only[i:i+4]:
            return True

    return False
