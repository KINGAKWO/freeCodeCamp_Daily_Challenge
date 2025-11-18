def is_match(fingerprint_a, fingerprint_b):
    """
    Check if two fingerprints match according to the given rules.
    
    Args:
        fingerprint_a (str): First fingerprint
        fingerprint_b (str): Second fingerprint
    
    Returns:
        bool: True if fingerprints match, False otherwise
    """
    # Quick length check
    if len(fingerprint_a) != len(fingerprint_b):
        return False
    
    length = len(fingerprint_a)
    print(length)
    # Calculate 10% threshold (ceiling division)
    max_allowed_differences = (length + 9) // 10
    print(max_allowed_differences)
    
    # Count differences with early termination
    differences = 0
    for char_a, char_b in zip(fingerprint_a, fingerprint_b):
        if char_a != char_b:
            differences += 1
            if differences > max_allowed_differences:
                print("differences")
                return False
    print("all good")           
    return True


is_match("helloworld", "jelloworld")
is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat")