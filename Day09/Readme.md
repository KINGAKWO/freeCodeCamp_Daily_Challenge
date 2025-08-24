**Character Battle**
================

A Python solution to the freeCodeCamp Daily Challenge: Character Battle

**Challenge Description**
-------------------------

Given two strings representing your army and an opposing army, each character from your army battles the character at the same position from the opposing army using the following rules:

* Characters a-z have a strength of 1-26, respectively.
* Characters A-Z have a strength of 27-52, respectively.
* Digits 0-9 have a strength of their face value.
* All other characters have a value of zero.
* Each character can only fight one battle.
* For each battle, the stronger character wins. The army with more victories, wins the war.

**Solution**
------------

The solution is implemented in the `battle` function, which takes two strings as input and returns the result of the battle.

**Example Use Cases**
--------------------

```python
print(battle("abc", "xyz"))  # "We lost"
print(battle("123", "456"))  # "We lost"
print(battle("ABC", "abc"))  # "We won"
print(battle("hello", "world"))  # "It was a tie"
```

**Code**
------

```python
def strength(ch):
    if 'a' <= ch <= 'z':
        return ord(ch) - ord('a') + 1
    elif 'A' <= ch <= 'Z':
        return ord(ch) - ord('A') + 27
    elif '0' <= ch <= '9':
        return int(ch)
    else:
        return 0

def battle(my_army, opposing_army):
    if len(my_army) > len(opposing_army):
        return "Opponent retreated"
    elif len(opposing_army) > len(my_army):
        return "We retreated"

    my_wins = 0
    opp_wins = 0

    for m, o in zip(my_army, opposing_army):
        my_strength = strength(m)
        opp_strength = strength(o)

        if my_strength > opp_strength:
            my_wins += 1
        elif opp_strength > my_strength:
            opp_wins += 1
        # If equal, no one wins

    if my_wins > opp_wins:
        return "We won"
    elif opp_wins > my_wins:
        return "We lost"
    else:
        return "It was a tie"
```

**Explanation**
-------------

The `strength` function calculates the strength of a character based on its ASCII value. The `battle` function uses the `strength` function to determine the winner of each battle and returns the result of the war.

**License**
-------

This code is licensed under the MIT License.

**Author**
-------
Akwo Makembe King "kingakwomakembe@gmail.com"