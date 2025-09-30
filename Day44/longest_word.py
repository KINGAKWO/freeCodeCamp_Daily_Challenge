import re


def get_longest_word(sentence):
    """
    Return the longest word in a sentence.

    - Ignores periods when determining word length.
    - If multiple words tie for longest, return the first occurrence.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The longest word found in the sentence.
    """
    # Extract words (ignores punctuation like periods)
    words = re.findall(r'\b\w+\b', sentence)

    # Find the first longest word
    return max(words, key=len)
