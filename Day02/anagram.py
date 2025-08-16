def are_anagrams(str1, str2):
    str1 = str1.replace(" ","")
    str2 = str2.replace(" ","")
    str1 = sorted(str1.lower().strip())
    str2 = sorted(str2.lower().strip())
    if  str1 == str2:
        print('it is an anagram')
        return True
    else:
        print("Not an anagram")
        

are_anagrams("listen", "silent")
are_anagrams("Hello", "World")
