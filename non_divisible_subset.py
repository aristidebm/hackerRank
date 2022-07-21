"""
[source](https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true)

Problem statement:
------------------
Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers in S' is not evenly divisible by k.

Example:
--------

S = [19, 10, 12, 24, 25, 22] k = 4
One of the arrays that can be created is S'[0] = [10, 12, 25]. Another is S'[1] = [19, 22, 24]. After testing all permutations, the maximum length solution array has 3 elements.

Input format description:
-------------------------
The first line contains 2 space-separated integers, n and k, the number of values in S and the non factor.
The second line contains n space-separated integers, each an S[i], the unique values of the set.

Output format description:
--------------------------
+ int: the length of the longest subset of S meeting the criteria.

constraints:
-----------
+ 1 <= n <= 10^5
+ 1 <= k <= 100
+ 1 <= S[i] <= 10^9
+ All of the given numbers are distinct.

Discussion:
-----------

This initially appears difficult to solve in reasonable time complexity. After further thought, I think this can be done on O(n) with a few considerations. This is supposed to be an "easy" problem, so I'll provide some algorithm guidance here.

For any number K, the sum of 2 values (A & B) is evenly divisible by K if the sum of the remainders of A/K + B/K is K. (There is also a special case where both A & B are evenly divisible, giving a sum of 0.)

For any such remainder, there is 1 and only 1 other remainder value which will make a sum divisible by K.

Example: with K of 5, remainder pairs are 1 + 4 & 2 + 3. Given the numbers with a remainder of 1, they can't be paired with ANY of the numbers with remainder 4 (and vice versa). So, for the number of values in the resultant set, choose the larger of values with remainder 1 vs. values with remainder 4. 
Choose the larger set of remainder 2 vs remainder 3.

For the special case where remainder is 0, given the set of all values which are individually divisible by K, they can't be paired with any others. So, at most 1 value which is evenly divisible by K can be added to the result set.

For even values of K, the equal remainder is similar to the 0 case. For K = 6, pairs are 1 + 5, 2 + 4, 3 + 3. For values with remainder 3, at most one value can be added to the result set.
"""

import math
import os
import random
import re
import sys
from collections import defaultdict

# Copied from hackerrank discussion


def nonDivisibleSubset(k, s):
    """
    This problem is pretty hard unless we notice this trick.
    + For all integers A, B and K such that A % K != 0 and B % K != 0
        (A + B) % K == 0 if and only if (A % K) + (B % K) == K.
    + Obviously if A % K == 0 and B % K == 0 then (A + B) % K == 0.

    Problem Solving Workflow
    ------------------------
    1. Group set numbers per remainders
    2. For two remainder r1 and r2 such that r1 != r2, we can add two numbers n1 and n2
    (such that r1 = n1 % K and r2 = n2 % k) if and and only if r1 + r2 != K. In which case
    we the maximum number between set that remainder equals r1 and sets that remainder equals r2.
    3. If r == k / 2 belongs to remainders then their can exist only on element of the set of
    numbers that remainder equals to r in the result set (since if their are two k / 2 + k / 2 == k)
    4. If r == 0 belongs to remainders then their can exist only on element of the set of numbers that
    remainder equals to r in the result set.
    """
    per_remainder = defaultdict(list)

    for item in s:
        per_remainder[item % k].append(item)

    # if set (s) contains only numbers that are evenly divisible
    # divisible by k, maximum subset that satisfy the problem condition
    # is of length 1.

    count = 0

    # Only one of the elements that are evenly divisible
    # by K can be added to set
    if len(per_remainder[0]) > 0:
        count = 1

    # Only one of the elements at index k/2 can be add
    # the output set.
    if len(per_remainder[k / 2]) > 0:
        count += 1

    # Create eventual divisor of k with their counter part so
    # that their sum equals k. (remove 0 and k/2 since their already processed)
    S = set((x, k - x) for x in range(1, k // 2 + 1) if x != k / 2)

    for i, j in S:
        # This can be safely done (without KeyError) cause per_remainder is a `defaultdict`.
        count += max(len(per_remainder[i]), len(per_remainder[j]))

    return count


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(str(result) + "\n")

    # fptr.close()
