"""
[source](https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true)

Problem statement:
-----------------

An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a 1 unit change in altitude. We define the following terms:

+ A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
+ A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Example:
-------

steps = 8paths = [DDUUUUDD]

      /\
_    /  \_
 \  /    
  \/

The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain 2 units high. Finally, the hiker returns to sea level and ends the hike.

8
UDDDUDUU

Explanation:
------------

_/\      _
   \    /
    \/\/

The hiker enters and leaves one valley.

Input format description:
-------------------------
+ The first line contains an integer steps, the number of steps in the hike.
+ The second line contains a single string path, of steps characters that describe the path.

Output format description:
--------------------------
int: the number of valleys traversed

Constraints:
------------
+ 2 <= steps <= 10 ^6
+ path[i] in {UD}

Clever Solution:
----------------
If the altitude is 0 and current step == 'U' then we are at sea level from zero.
```python
def counting_valleys(steps, path):
    altitude = 0
    num_valleys = 0
    for v in path:
        
        if v == "U":
            altitude += 1
        else:
            altitude -= 1

        if v == "U" and altitude == 0:
            num_valleys += 1

    return num_valleys
"""
import math
import os
import random
import re
import sys


# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path


def counting_valleys(steps, path):
    # The idea is to transform the problem into peak finding one.
    sea = 0
    valley_count = 0
    new_path = []

    for idx, v in enumerate(path):
        if v == "D":
            sea -= 1
            new_path.append(sea)
        else:
            sea += 1
            new_path.append(sea)

    ref = 0

    for idx, v in enumerate(new_path):
        if v == 0:
            if sum(new_path[ref:idx]) < 0:
                valley_count += 1
            ref = idx

    return valley_count


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = counting_valleys(steps, path)

    print(str(result) + "\n")

    # fptr.close()
