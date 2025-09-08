def build_acronym(s):
    word = s.split()
    ignore = ['a',"for","an","and","by","of"]
    acronym = []

    for idx, i in enumerate(word):
        if i.lower() in ignore and idx!=0:
           continue
        else:
            acronym.append(i[0].upper())
    return "".join(acronym)





build_acronym("National Aeronautics and Space Administration")
build_acronym("Search Engine Optimization")
build_acronym("For your information")