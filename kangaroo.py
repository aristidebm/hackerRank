"""
[source](https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true&h_r=next-challenge&h_v=zen)

Problem statement
-----------------
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

+ The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
+ The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.

You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

Examples
--------
+ x1 = 2, v1 = 1
+ x2 = 1, v2 = 2
After one jump, they are both at x=3, (x1 + v1 = 3, x2 + v2 = 3), so the answer is YES.

Input Format Description
------------------------
A single line of four space-separated integers denoting the respective values of x1, v1, x2 and v2.

Output Format Description
-------------------------
string: either YES or NO

Constraints
-----------
+ 0 <= x1 < x2 <= 10000
+ 1 <= v1 <= 10000
+ 1 <= v2 <= 10000
"""

import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    res = False

    while 1 <= x1 + v1 <= 19999 and 2 <= x2 + v2 <= 20000:
        x1, x2 = x1 + v1, x2 + v2
        if x1 == x2:
            res = True
            break

    return f"{'YES' if res else 'NO'}"


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result + "\n")
    # fptr.write(result + '\n')

    # fptr.close()
