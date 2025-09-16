def capitalize(paragraph):
    capitalize_next = True
    result = []
    for char in paragraph:
        if capitalize_next and char.isalpha():
            result.append(char.upper())
            capitalize_next = False
            continue
        result.append(char)

        if char in ".?!":
            capitalize_next = True

    return "".join(result)