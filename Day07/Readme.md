
**Mile Pace Calculator**
=======================

A Python solution to calculate the average time it took to run each mile.

**Challenge Description**
-------------------------

Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took to run those miles, return a string for the average time it took to run each mile in the format "MM:SS".

**Solution**
------------

The solution is implemented in the `mile_pace` function, which takes two parameters: `miles` (the number of miles ran) and `duration` (the time it took to run those miles in "MM:SS" format).

**Example Use Cases**
--------------------

```python
print(mile_pace(3, "24:00"))  # Output: "08:00"
```

**Code**
------

```python
def mile_pace(miles, duration):
    minutes, seconds = map(int, duration.split(":"))
    total_seconds = minutes * 60 + seconds
   
    avg_seconds_per_mile = total_seconds // miles  
    pace_minutes, pace_seconds = divmod(avg_seconds_per_mile, 60)
    
    return f"{pace_minutes:02d}:{pace_seconds:02d}"
```

**Explanation**
-------------

The `mile_pace` function first splits the input duration into minutes and seconds, then calculates the total number of seconds. It then calculates the average number of seconds per mile by dividing the total seconds by the number of miles.

Finally, it converts the average seconds per mile back into minutes and seconds, and returns the result as a string in "MM:SS" format.

**License**
-------

This code is licensed under the MIT License.