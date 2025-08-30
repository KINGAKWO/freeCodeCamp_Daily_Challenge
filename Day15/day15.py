def find_duplicates(arr):
    seen = set()
    duplicates = []
     
    for num in arr:
         if num in seen:
             if num not in duplicates:
                duplicates.append(num)
             
         else:
             seen.add(num)
    print(duplicates)
    return sorted(duplicates)

find_duplicates([1, 2, 3, 4, 5])
find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4])