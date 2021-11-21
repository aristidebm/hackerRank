"""
[source](https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true)

Problem statement
-----------------
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Examples
--------
arr = [1, 3, 5, 7, 9]

The minimum sum is (1 + 3 + 5 + 7) and the maximum sum is (3 + 5 + 7 + 9) . The function prints

Input Format Description
------------------------
A single line of five space-separated integers.

Output Format Description
-------------------------
Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

Constraints
-----------
1 <= arr[i] <= 10^9
"""
import math
import os
import random
import re
import sys


def mini_max_sum(arr):
    """
    tip: the problem is simple if the array is sorted
    the sum of 4-first integers is the minimum sum and
    the sum of 4-last  integers is the maximum sum
    """
    arr = sorted(arr)
    maxi = sum(arr[1 : len(arr)])
    mini = sum(arr[0 : len(arr) - 1])
    print(f"{mini} {maxi}")


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))
    mini_max_sum(arr)
