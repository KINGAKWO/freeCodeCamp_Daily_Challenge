def jbelmu(text):
    jumbled_words = []
    text = text.lower().split()

    for word in text:
        if len(word) < 3:
            jumbled_words.append(word)
        else:
            first_letter = word[0]
            last_letter = word[-1]
            middle_letters = word[1:-1]
            sorted_middle_letters = sorted(middle_letters)
            jumbled_word=f"{first_letter}{''.join(sorted_middle_letters)}{last_letter}"
            jumbled_words.append(jumbled_word)
    return ' '.join(jumbled_words)


