def all_unique(s):
    char = list(s) 
    unique = set(s) 
    if len(char)==len(unique):
        print("unique ") 
        return True
    else:
        print("characters are not unique in string") 
        return False