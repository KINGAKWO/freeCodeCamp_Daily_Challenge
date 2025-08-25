import re 
def to_camel_case(s):
    camel = []
    words = [w for w in re.split(r"[ _-]+", s.strip()) if w]
    for i, word in enumerate(words) :
        if i == 0:
            first_word = word.lower()
            camel.append(first_word)
        else:
            first_letter = word[0][0].upper()
            others= word[1:].lower()
            camel.append(first_letter+others)
            
    return ''.join(camel)
            

            
        
        
        

        

to_camel_case("hello world")
to_camel_case("FREE cODE cAMP")
to_camel_case("HELLO WORLD")
to_camel_case("secret agent-X")
to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk")