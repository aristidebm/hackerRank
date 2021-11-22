"""
[source](https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true)

Problem statement
-----------------
You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Examples
--------
candles = [4, 4, 3, 1]

The maximum height candles are  units high. There are  of them, so return.

Input Format Description
------------------------
The first line contains a single integer, n , the size of candles[]
The second line contains n space-separated integers, where each integer i describes the height of candles[i].

Output Format Description
-------------------------
int: the number of candles that are tallest

constraints
-----------

+ 1 <= n <= 10^5
+ 1 <= candles[i] <= 10^7
"""

import math
import os
import random
import re
import sys

def birthday_cake_candles(candles):
	"""
	The idea is to use a dictionnary to count the number of
	occurence of each number and take the maximum key with it value
	"""
	candles_map = {}

	# init candle map
	for candle in candles:
		candles_map[candle] = 0

	# count the number of candles
	for candle in candles:
		candles_map[candle] += 1

	max_candle = max(candles)

	return candles_map[max_candle]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthday_cake_candles(candles)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
