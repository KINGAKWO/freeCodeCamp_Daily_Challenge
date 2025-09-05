def repeat_vowels(s):
    vowels = set("aeiouAEIOU")  
    vowel_count = 0             
    result = []                  

    for char in s:               
        if char in vowels:
            vowel_count += 1
            repeated = char + char.lower() * (vowel_count - 1)
            result.append(repeated)
        else:
            result.append(char)  

    return ''.join(result)       
