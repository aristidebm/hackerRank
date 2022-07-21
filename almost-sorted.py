#!/bin/python3
"""
[source](https://www.hackerrank.com/challenges/almost-sorted/problem)
"""

import math
import os
import random
import re
import sys
import operator


#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
# Algorithm
# 1. Find Wrong  index looping through arr from left to right.
# 2. Find Wrong index looping through arr from right to left.
# 3. Swap the two indexes and check if the array is sorted.
# 4. if the array isn't sorted, swap element arr[k], arr[leftWrongIndex + rightWrongIndex - k] for k in [leftWrongIndex, ((leftWrongIndex + rightWrongIndex) // 2 + 1)]
# 5. check if the array is sorted, if not print no


class Solution:
    def almostSorted(self, arr):

        if self.isSorted(arr):
            print("yes")
            return

        rightWrongIndex = self.findRightWrongIndex(arr)
        leftWrongIndex = self.findLeftWrongIndex(arr)

        if self.isSorted(self.swap(arr[:], leftWrongIndex, rightWrongIndex)):
            print("yes")
            print(f"swap {leftWrongIndex + 1} {rightWrongIndex + 1}")
            return

        # An array can be sorted in ascending order using reverse if and only if the array is already sorted in
        # descending order from leftWrongIndex to rightWrongIndex.
        middleIndex = math.ceil((leftWrongIndex + rightWrongIndex) / 2)
        k = leftWrongIndex

        while k < middleIndex:
            self.swap(arr, k, leftWrongIndex + rightWrongIndex - k)
            k += 1

        if self.isSorted(arr):
            print("yes")
            print(f"reverse {leftWrongIndex + 1} {rightWrongIndex + 1}")
            return

        print("no")

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
        return arr

    def findLeftWrongIndex(self, arr):
        idx = 0
        while idx < len(arr) - 1 and arr[idx] < arr[idx + 1]:
            idx += 1
        return idx

    def findRightWrongIndex(self, arr):
        idx = len(arr) - 1
        while idx > 0 and arr[idx] > arr[idx - 1]:
            idx -= 1
        return idx

    def isSorted(self, arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True


if __name__ == "__main__":
    n = int(input().strip())
    array = list(map(int, input().rstrip().split()))
    s = Solution()
    s.almostSorted(array)


def almostSorted(self, arr):

    if self.isSorted(arr):
        print("yes")
        return

    rightWrongIndex = self.findRightWrongIndex(arr)
    leftWrongIndex = self.findLeftWrongIndex(arr)

    if self.isSorted(self.swap(arr[:], leftWrongIndex, rightWrongIndex)):
        print("yes")
        print(f"swap {leftWrongIndex + 1} {rightWrongIndex + 1}")
        return

    # An array can be sorted in ascending order using reverse if and only if the array is already sorted in
    # descending order from leftWrongIndex to rightWrongIndex.
    middleIndex = math.ceil((leftWrongIndex + rightWrongIndex) / 2)
    k = leftWrongIndex

    while k < middleIndex:
        self.swap(arr, k, leftWrongIndex + rightWrongIndex - k)
        k += 1

    if self.isSorted(arr):
        print("yes")
        print(f"reverse {leftWrongIndex + 1} {rightWrongIndex + 1}")
        return

    print("no")


def swap(self, arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def findLeftWrongIndex(self, arr):
    idx = 0
    while idx < len(arr) - 1 and arr[idx] < arr[idx + 1]:
        idx += 1
    return idx


def findRightWrongIndex(self, arr):
    idx = len(arr) - 1
    while idx > 0 and arr[idx] > arr[idx - 1]:
        idx -= 1
    return idx


def isSorted(self, arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
