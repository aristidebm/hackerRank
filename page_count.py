"""
(source)[https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true]

Problem Statement
-----------------

A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the book. They always turn pages one at a time. When they open the book, page 1 is always on the right side.

When they flip page 1, they see pages 2 and 3. Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book. If the book is n pages long, and a student wants to turn to page p, what is the minimum number of pages to turn? They can start at the beginning or the end of the book.

Given n and p, find and print the minimum number of pages that must be turned in order to arrive at p page.

Example:
--------
Using the diagram above, if the student wants to get to page 3, they open the book to page 1, flip 1 page and they are on the correct page. If they open the book to the last page, page 5, they turn 1 page and are at the correct page. Return 1.

6
2

1
If the student starts turning from page 1, they only need to turn 1 page.
If a student starts turning from page 6, they need to turn 2 pages.

The minimum page to turn is min(1, 2) = 1

Input format description:
-------------------------
The first line contains an integer n, the number of pages in the book.
The second line contains an integer, p, the page to turn to.

Output format description:
--------------------------
+ int: the minimum number of pages to turn

constraints
-----------
+ 1 <= n <= 10^5
+ 1 <= p <= n.

Improved solution
-----------------
```python
return min(p // 2, n//2 - p//2)

+ p//2: is the number of page turns.
+ n//2: is the total number of page turns.
```
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def page_count(n, p):
    return min(p // 2, (n + 1 - p) // 2 if n % 2 == 0 and n - p == 1 else (n - p) // 2)


4
if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = page_count(n, p)

    print(str(result) + "\n")

    # fptr.close()
