from collections import Counter 
import string
def get_words(paragraph):
    words =paragraph.lower().translate(str.maketrans('','',string.punctuation)).split()        
    occurence = Counter(words).most_common(3)
    most_frequent = [word for word, count in occurence] 

    print (most_frequent)
    return most_frequent



get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding")
get_words("I like coding. I like testing. I love debugging!")