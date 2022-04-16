[source](https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=true)


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#
# Tips:
# -----
#  Since "swap operation does not change the number of balls in any container", after all swaps,
#  the resulting number of balls in each container should still be the same. That means,
#  each type needs to occupy any one of the containers. If there is a missmatch,
#  it means that type of ball has nowhere else to go and the answer is impossible.
# The way to approach these kind of problems is to see what thinks remain constant
#  between the sample input and sample solution. Most of the medium level problems on here are similar.
# To boost your confidence, try to solve the swap nodes problem below by thinking this way.
# https://www.hackerrank.com/challenges/swap-nodes-algo/problem

def organizingContainers(container):
    predicate = {sum(row) for row in container}.symmetric_difference(sum(col) for col in zip(*container))
    return "Possible" if not predicate else "Impossible"

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result + '\n')
