#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#
# Algorithm :
# 1. On genere un tableau des "n" premiers entiers P.
# 2. Pour chaque P[i], on cherche un element j tel que |P[j] - i| = k.
# 3. Si un tel element existe, echanger P[i] et P[j].
# 4. Sinon renvoyer - 1 car Pour tout i, il doit exister cet element j pour qu'on puisse parler de permutation absolue.

# Fail for time limit exceed : O(n ^ 2)
def absolutePermutation(n, k):
    P = list(range(1, n + 1))

    for i, el in enumerate(P, start=1):

        if abs(P[i - 1] - i) == k:  # nothing to do.
            continue

        for j in range(i, n):  # list is 0-based index, we have to reduce by one.
            if abs(P[j] - i) == k:
                P[j], P[i - 1] = P[i - 1], P[j]
                break

        # If j == n - 1 and we haven't swap that means we have not found j so that |P[j] - i| = k
        # we must return - 1
        if j == n - 1 and abs(P[i - 1] - i) != k:
            return [-1]

    return P


# Optimized solution : O(n)
def absolutePermutation(n, k):
    P = list(range(1, n + 1))
    i = 1
    while (j := k + i) <= n:
        if abs(P[i - 1] - i) == k:
            i += 1
            continue
        elif abs(P[j - 1] - i) == k:
            P[j - 1], P[i - 1] = P[i - 1], P[j - 1]
            i += 1
            continue

        return [-1]

    if not all(abs(P[i] - (i + 1)) == k for i in range(n)):
        return [-1]

    return P


if __name__ == "__main__":

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        print(" ".join(map(str, result)))
        print("\n")
