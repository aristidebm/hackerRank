#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

# Simply Explained, this problem is a problem of pattern matching in a grid.

# Naive approach
# --------------
# 1. Generate all sub-matrix of G that have the order of P
# 2. For Each Generated matrix, compare the matrix with P.
# But regarding the provided constraints (len(G) and len(P) can reach 1000),
# that can be a costly approach. We have to think differently.

# A Way Better Approach
# ---------------------

# 1. Take the first row of P and try to find it in G with index Key
# 2. If not Found, print "NO" to the screen.
# 3. If found, store the beginIndex, endIndex and rowIndex founded key and increment Key with 1 (second line of P)
# 4. Compare each row[beginIndex:endIndex + 1] of G beginning at rowIndex + 1 with each line of P beginning at Key + 1
# 5. If all these lines matches, then we found our pattern, otherwise, the pattern doesn't exist in the grid.

# FIX
# ----

# With The above approach, all the logic belongs on whether we find the first line of P in  G or not,
# but what happen when this line appears in multiple places in G ? To Fix that, we must list all places that the
# first line of P appears in G and apply for each the provided approach.

#  We can be sure with the constraints that len(P) <= len(G) and len(P[0]) <= len(G[0])


def gridSearch(G, P):
    key = 0
    rowIndexes = []
    PR = len(P)
    GR = len(G)
    # Find all matching row's index in G of the first row of P.
    for rowIndex, row in enumerate(G):
        if P[key] in row:
            indexes = findBeginEndIndex(rowIndex, row, P[key])
            rowIndexes.extend(indexes)

    # The pattern can't exists if we can't find the matching of the first row of P.
    if not rowIndexes:
        return "NO"

    # Try to find the pattern with each rowIndex, and the window [beginIndex, endIndex] stop at the first found.
    for rowIndex, beginIndex, endIndex in rowIndexes:
        while key < PR and rowIndex < GR:
            if P[key] == G[rowIndex][beginIndex : endIndex + 1]:
                key += 1
                rowIndex += 1
            else:
                break

        if key == PR:
            # We found a pattern, print Yes and stop the program
            return "YES"
        else:
            # We don't found we this row index, so try with the following rowIndex
            key = 0
            continue

    return "NO"


def findBeginEndIndex(index, phrase, pattern):
    # Iteratively find the first Index of all occurrence in the row
    indexes = []
    word = phrase
    try:
        # -1 is used only to accept Index of value 0, it can be - 2  or any other negative number
        while (beginIndex := word.find(pattern)) > -1:
            endIndex = beginIndex + len(pattern) - 1
            indexes.append((index, beginIndex, endIndex))
            # The can be to replace all the pattern, but to it like this, can hide the detection of the pattern
            # Example:
            # 1
            # 5 15
            # 111111111111111
            # 111111111111111
            # 111111011111111
            # 111111111111111
            # 111111111111111
            # 3 5
            # 11111
            # 11111
            # 11110
            word = word.replace(pattern[0], "*", 1)
    except IndexError:
        pass

    return indexes


if __name__ == "__main__":

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        print(result + "\n")

# while x := value():
#     # do()
#
# # is equivalent to
#
# x = value()
# while x:
#     x = value() # End Of Line
# 1
# 4 6
# 123412
# 561212
# 123634
# 781288
# 2 2
# 12
# 34
