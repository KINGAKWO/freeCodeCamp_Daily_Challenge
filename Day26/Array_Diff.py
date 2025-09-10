def array_diff(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    diff = list(set1^set2)
    diff.sort()
    print(f"diff{diff}")
    return diff




array_diff(["apple", "banana"], ["apple", "banana", "cherry"])
array_diff(["apple", "banana", "cherry"], ["apple", "banana"])
array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"])
array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"])