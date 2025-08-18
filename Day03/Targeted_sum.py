def find_target(arr, target):
    for i in range(len(arr)-1):
        if i < len(arr)-1:
            for j in range(i + 1, len(arr)): 
                if j<len(arr):
                    sum = arr[i] + arr[j]
                    if sum == target:
                        return [i,j]
    return "Target not found"

