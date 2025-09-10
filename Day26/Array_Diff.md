# Array Diff

A Python solution to the freeCodeCamp Daily Challenge: Array Diff

## Challenge Description

Given two arrays with string values, return a new array containing all the values that appear in only one of the arrays. The returned array should be sorted in alphabetical order.

## Solution

The solution is implemented in the `array_diff` function, which takes two lists of strings as input and returns a sorted list of strings that are unique to each list (symmetric difference). It uses Python's set operations for efficiency.

## Example Use Cases

```python
array_diff(["apple", "banana"], ["apple", "banana", "cherry"])  # Returns: ["cherry"]
array_diff(["apple", "banana", "cherry"], ["apple", "banana"])  # Returns: ["cherry"]
array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"])  # Returns: ["eight", "four", "six", "two"]
array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"])  # Returns: ["five", "one", "seven", "three"]
```

## Tests

The function passes the following test cases:
- Passed: array_diff(["apple", "banana"], ["apple", "banana", "cherry"]) should return ["cherry"].
- Passed: array_diff(["apple", "banana", "cherry"], ["apple", "banana"]) should return ["cherry"].
- Passed: array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]) should return ["eight", "four", "six", "two"].
- Passed: array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"]) should return ["five", "one", "seven", "three"].
- Passed: array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]) should return ["freeCodeCamp", "rocks"].

## Code

```python
def array_diff(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    diff = list(set1 ^ set2)
    diff.sort()
    print(f"diff{diff}")
    return diff
```

## License

This code is licensed under the MIT License.

## Author

AKWO MAKEMBE kING kingakwomakembe@gmail.com
"
