# [source](https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true)
# [doc](https://www.nayuki.io/page/next-lexicographical-permutation-algorithm)
#
# Algorithm:
# 1. Find largest index i such that array[i − 1] < array[i].
# (If no such i exists, then this is already the last permutation.)
#
# 2. Find largest index j such that j ≥ i and array[j] > array[i − 1].
#
# 3. Swap array[j] and array[i − 1].
#
# 4. Reverse the suffix starting at array[i].
#

import math
import os
import random
import re
import sys
import itertools

# # My Solution (Fail for timeout)

# def biggerIsGreater(w):
#     permutations = set(["".join(c) for c in itertools.permutations(w)])
#     permutations = sorted(list(permutations))
#     index = permutations.index(w) + 1
#     return (
#         "no answer"
#         if index == len(permutations) or len(permutations) == 1
#         else permutations[index]
#     )


# Optimized Solution
def biggerIsGreater(word):
    # Find non-increasing suffix

    if not word.replace(word[0], ""):
        return "no answer"

    suff_head = len(word) - 1

    while suff_head > 0 and word[suff_head - 1] >= word[suff_head]:
        suff_head -= 1

    if suff_head <= 0:
        return "no answer"

    # Find successor to pivot
    succ_pivot = len(word) - 1

    while word[succ_pivot] <= word[suff_head - 1]:
        succ_pivot -= 1

    word = list(word)
    word[suff_head - 1], word[succ_pivot] = word[succ_pivot], word[suff_head - 1]
    # Reverse suffix
    word[suff_head:] = reversed(word[suff_head:])
    return word


if __name__ == "__main__":

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result + "\n")
