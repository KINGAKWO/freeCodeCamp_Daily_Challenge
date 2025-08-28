**Laptop Budget Challenge**
==========================

A Python solution to the freeCodeCamp Daily Challenge: Laptop Budget

**Challenge Description**
-------------------------

Given an array of integers representing the price of different laptops, and an integer representing your budget, return:

* The second most expensive laptop if it is within your budget, or
* The most expensive laptop that is within your budget, or
* 0 if no laptops are within your budget.
* Duplicate prices should be ignored.

**Solution**
------------

The solution is implemented in the `get_laptop_cost` function, which takes two inputs:

* `laptops`: a list of integers representing the prices of different laptops
* `budget`: an integer representing your budget

The function returns the second most expensive laptop if it is within your budget, or the most expensive laptop that is within your budget, or 0 if no laptops are within your budget.

**Example Use Cases**
--------------------

```python
print(get_laptop_cost([100, 200, 300, 400], 250))  # 200
print(get_laptop_cost([100, 200, 300, 400], 500))  # 400
print(get_laptop_cost([100, 200, 300, 400], 50))   # 0
```

**Code**
------

```python
def get_laptop_cost(laptops, budget):
    prices = sorted(set(laptops), reverse=True)

    if len(prices) >= 2:
        second_best = prices[1]
        if second_best <= budget:
            return second_best

    affordable = [p for p in prices if p <= budget]
    return max(affordable) if affordable else 0
```

**License**
-------

This code is licensed under the MIT License.

**Author**
-------
Akwo Makembe King "kingakwomakembe@gmail.com"