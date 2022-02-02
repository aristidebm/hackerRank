"""
[source](https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true)

Problem statement
-----------------
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example:
--------
n = 7
arr = [1, 2, 1, 2, 1, 3, 2]
There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

Input format description:
-------------------------
The first line contains an integer n, the number of socks represented in arr.
The second line contains n space-separated integers, arr[i], the colors of the socks in the pile.

Output format description:
--------------------------
+ int: the number of pairs 

constraints
-----------
+ 1 < n <= 100
+ 1 <= arr[i] <= 100 where 0 <= i < n

Improved solution ()
--------------------
```python
def sock_merchant(n, ar):
    return sum([ar.count(i)//2 for i in set(ar)])
```

What do you Learn New ?
-----------------------
The logic that is used is with defaultdict structure
is in reality an already defined Structure in python `collections` module that is called `Counter`.

[source](https://docs.python.org/3/library/collections.html#counter-objects)

A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.
"""
import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sock_merchant(n, ar):
    pairs = defaultdict(int)
    for i in ar:
        pairs[i] += 1
    pairs = [pairs[k] // 2 for k in pairs]
    return sum(pairs or [0])


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sock_merchant(n, ar)

    print(str(result) + "\n")

    # fptr.close()
