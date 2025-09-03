def is_pangram(sentence, letters):
    sen = sentence.lower()
    let = letters.lower()

    sentence_letters = {char for char in sen if char.isalpha() and char.isascii()}

    allowed_letters = {char for char in let if char.isalpha() and char.isascii()}

    return sentence_letters == allowed_letters