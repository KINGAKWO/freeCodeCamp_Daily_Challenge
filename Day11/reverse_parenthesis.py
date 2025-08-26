import re

def decode(s):
    while re.search(r"\([^()]*\)", s):
        matches = re.findall(r"\([^()]*\)", s)
        for match in matches:
            inner = match[1:-1]
            # Reverse the inside
            reversed_inner = inner[::-1]
            # Replace this exact match with its reversed inner
            s = s.replace(match, reversed_inner, 1)
    return s

