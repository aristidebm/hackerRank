"""
[source](https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true)

Problem statement
-----------------
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

Examples
--------

scores = [12, 24, 10, 24]
Scores are in the same order as the games played. She tabulates her results as follows:
																	
													Count
	Game 	Score 	Minimum		Maximum			Min 		Max
	0 		12 		12 			12 				0 			0
	1 		24     	12 			24 				0 			1
	2 		10 		10 			24 				1 			1
	3 		24 		10 			24 				1 			1

Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

Input Format Description
------------------------
+ The first line contains an integer n, the number of games.
+ The second line contains  space-separated integers describing the respective values of score[0], score[1], ..., score[n-1]

Output Format Description
-------------------------
int[2]: An array with the numbers of times she broke her records. Index 0 is for breaking most points records, and index 1 is for breaking least points records.

Constraints
-----------
+ 1 <= n <= 1000
+ 0 <= scores[i] <= 10^8
"""

import math
import os
import random
import re
import sys


def breaking_records(scores):
    mini, maxi = scores[0], scores[0]
    mini_break, maxi_break = 0, 0

    for score in scores[1:]:
        if score < mini:
            mini = score
            mini_break += 1

        if score > maxi:
            maxi = score
            maxi_break += 1

    return [maxi_break, mini_break]


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breaking_records(scores)

    print(" ".join(map(str, result)))
    print("\n")

    # fptr.close()
# 10
# 3 4 21 36 10 28 35 5 24 42
# 9
# 10 5 20 20 4 5 2 25 1
