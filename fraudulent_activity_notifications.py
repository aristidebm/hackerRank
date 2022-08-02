"""
[source](https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?isFullScreen=true)
"""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

# Failed for time limit exceeded, optimize the solution.

# Algorithm:
# 1. Initialize the number of notifications to 0
# 2. Initialize a fixed size window of size d beginIndex = 0, endIndex = d - 1
# 3. find the median of Array[beginIndex: EndIndex]
# 4. Compare the number at index endIndex + 1 with the 2 * median
# 5. If Array[endIndex + 1] >= 2 * median, increment the number of notifications
# 6. Move the window, one step in the right direction.
# 7. Repeat step 3 to 6 until endIndex reach the end of the array.
# 8. return the number of notifications


def activityNotifications(expenditure, d):
    # Write your code here
    L = len(expenditure)
    beginIndex = 0
    endIndex = d - 1
    numberOfNotification = 0

    while endIndex < L - 1:
        median = computeMedian(expenditure[beginIndex : endIndex + 1])
        if expenditure[endIndex + 1] >= 2 * median:
            numberOfNotification += 1
        beginIndex += 1
        endIndex += 1

    return numberOfNotification


def computeMedian(arr):
    arr = sorted(arr)
    L = len(arr)
    if L % 2 != 0:
        return arr[L // 2]
    return (arr[L // 2 - 1] + arr[L // 2]) / 2


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result) + "\n")

    # fptr.close()
