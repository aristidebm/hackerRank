"""
[source](https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true)

Problem statement:
------------------
An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

+ The player with the highest score is ranked number 1 on the leaderboard.
+ Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

Example:
--------
ranked = [100, 90, 90, 80]
player = [70, 80, 105]

The ranked players will have ranks 1, 2, 2, and 3, respectively. If the player's scores are 70, 80 and 105, their rankings after each game are 4th, 3th, and 1st. Return [4, 3, 1].

Input format description:
-------------------------
The first line contains an integer "n", the number of players on the leaderboard.
The next line contains "n" space-separated integers "randed[i]", the leaderboard scores in decreasing order.
The next line contains an integer, "m", the number games the player plays.
The last line contains "m" space-separated integers "player[i]", the game scores.


Output format description:
--------------------------
int[m]: the player's rank after each new score

constraints
-----------
+ 1 <= n <= 2 x 10^5
+ 1 <= m <= 2 x 10^5
+ 0 <= ranked[i] <= 10^9 for 0 <= i <= n 
+ 0 <= player[j] <= 10^9 for 0 <= j <= n
+ The existing leaderboard, "ranked", is in descending order.
+ The player's scores, "ascending", are in ascending order.
"""

# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    ranks = []
    ranked = sorted(set(ranked), reverse=True)
    len_ = len(ranked)
    # remove duplicate
    for key in player:
        if key >= ranked[0]:
            ranks.append(1)
        elif key < ranked[len_ - 1]:
            ranks.append(len_ + 1)
        elif key == ranked[len_ - 1]:
            ranks.append(len_)
        else:
            ranks.append(binarySearch(key, ranked))

    return ranks


def binarySearch(key, ranked):
    len_ = len(ranked) - 1
    a, b = 0, len_

    while a <= b:
        rank = (a + b) // 2

        if ranked[rank] == key:
            return rank + 1

        if 0 < rank <= len_ and ranked[rank - 1] > key > ranked[rank]:
            return rank + 1

        if 0 <= rank < len_ and ranked[rank] > key > ranked[rank + 1]:
            return rank + 2

        if key < ranked[rank]:
            a = rank + 1

        if key > ranked[rank]:
            b = rank - 1


def main():
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
