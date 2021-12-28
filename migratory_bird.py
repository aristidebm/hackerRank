"""
[source](https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true&h_r=next-challenge&h_v=zen)

Problem Statement
-----------------

Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

Examples
--------
arr = [1, 1, 2, 2, 3]

There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1.

Input Format Description
------------------------
The first line contains an integer, n, the size of arr.
The second line describes arr as n space-separated integers, each a type number of the bird sighted.

Output Format Description
-------------------------
int: the lowest type id of the most frequently sighted birds
"""
import math
import os
import random
import re
import sys
from collections import defaultdict


def migratory_birds(arr):
    # Write your code here
    bird_count_by_type = defaultdict(int)
    for typ in arr:
        bird_count_by_type[typ] += 1

    max_sighted = max(bird_count_by_type.values())
    return min(
        filter(lambda x: bird_count_by_type[x] == max_sighted, bird_count_by_type)
    )


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratory_birds(arr)

    print(str(result) + "\n")

    # fptr.close()
