import re

def generate_slug(text):
    #Convert to lowercase
    text = text.lower()
    # Remove all characters except letters, numbers, and spaces
    text = re.sub(r'[^a-z0-9 ]', '', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
     # Strip leading/trailing spaces
    text = text.strip()
    # Replace spaces with %20
    text = text.replace(' ', '%20')
    
    return text

print(generate_slug("  ?H^3-1*1]0! W[0%R#1]D  "))