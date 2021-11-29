"""
[source](https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true&h_r=next-challenge&h_v=zen)

Problem statement
-----------------
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
Lily decides to share a contiguous segment of the bar selected such that:
+ The length of the segment matches Ron's birth month, and,
+ The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.

Examples
--------
s = [2, 2, 1, 3, 2]
d = 4
m = 2

Lily wants to find segments summing to Ron's birth day, d = 4 with a length equalling his birth month, m = 2. In this case, there are two segments meeting her criteria: [2, 2] and [1, 3].

Input Format Description
------------------------
+ The first line contains an integer , the number of squares in the chocolate bar.
+ The second line contains n space-separated integers s[i], the numbers on the chocolate squares where 0 <= i < n.
+ The third line contains two space-separated integers, d and m, Ron's birth day and his birth month.

Output Format Description
-------------------------
+ int: the number of ways the bar can be divided

Constraints
-----------
+ 1 <= n <= 100
+ 1 <= s[i] <= 5 (where 0 <= i < n)
+ 1 <= d <= 31
+ 1 <= m <= 12 
"""

import math
import os
import random
import re
import sys


def birthday(s, d, m):
    division = 0
    begin = 0
    while m + begin <= len(s):
        if sum(s[begin : m + begin]) == d:
            division += 1
        begin += 1

    return division


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(str(result) + "\n")

    # fptr.close()
