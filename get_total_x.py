"""
[source](https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen)

Problem statement
-----------------
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

1. The elements of the first array are all factors of the integer being considered.
2. The integer being considered is a factor of all elements of the second array.

These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

Examples
--------
a = [2, 6]
b = [24, 36]

There are two numbers between the arrays:  6 and 12.
6%2 = 0 6%6 = 0 and 36%6 = 0 24%6 = 0 for the first value.
12%2 = 0 12%6 = 0 and 36%12 = 0 24%12 = 0 for the second value.
Return 2

Input Format Description
------------------------
+ The first line contains two space-separated integers, n and m, the number of elements in arrays a and b.
+ The second line contains n distinct space-separated integers a[i] where 0 <= i < n.
+ The second line contains m distinct space-separated integers b[j] where 0 <= j < m.

Constraints
-----------
+ 1 <= n, m <= 10
+ 1 <= a[i] <= 100
+ 1 <= b[j] <= 100
"""

import math
import os
import random
import re
import sys


def getTotalX(a, b):
    res = 0
    for i in range(1, 10_000):
        if _is_divisor(i, b) and _is_multiple(i, a):
            res += 1
    return res


def _is_divisor(item, b):
    return all([j % item == 0 for j in b])


def _is_multiple(item, a):
    return all([item % i == 0 for i in a])


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(str(total) + "\n")

    # fptr.close()
