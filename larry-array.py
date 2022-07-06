#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

# This can be solved using 15-puzzle solvable (https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/)
# The puzzle is solvable under below conditions
#  1. If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
#  2. If N is even, puzzle instance is solvable if
#    + the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is odd.
#    + the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is even.
#    + For all other cases, the puzzle instance is not solvable.

# In our case, N = 3 which is odd, so we just have to compute the number of inversion and check whether it is even or not
# 1. if it is even, we can sort with rotation
# 2. otherwise, we cannot sort it.

def larrysArray(A):
    number_of_inversion = 0
    len_ = len(A)
    for i in range(len_):
        for j in range(i + 1, len_):
            if A[i] > A[j]:
                number_of_inversion += 1

    return "YES" if number_of_inversion % 2 == 0 else "NO"


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        print(result + '\n')
