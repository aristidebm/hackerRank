"""
[source](https://www.hackerrank.com/challenges/countingsort4/problem?isFullScreen=true)

"""

#!/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#


def countSort(arr):
    # Write your code here
    A = len(arr)
    arr = [(x[0], "-") if idx < A // 2 + 1 else x for idx, x in enumerate(arr, 1)]
    arr = sorted(arr, key=itemgetter(0))
    print(" ".join([x[1] for x in arr]))


if __name__ == "__main__":
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
