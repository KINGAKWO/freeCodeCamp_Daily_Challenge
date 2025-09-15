<<<<<<< HEAD
from collections import Counter 
def squares_with_three(n):
    target = '3'
    count = 0
    for num in range(1,n+1):
        square = num**2
        my_list = list(str(abs(square)))
        if target in my_list:
            count += 1
    return count 


squares_with_three(10)

squares_with_three(10000)

=======
from collections import Counter 
def squares_with_three(n):
    target = '3'
    count = 0
    for num in range(1,n+1):
        square = num**2
        my_list = list(str(abs(square)))
        if target in my_list:
            count += 1
    return count 


squares_with_three(10)

squares_with_three(10000)

>>>>>>> ec33a251652659f92073ba3ed7671739354a1f88
