"""
[source](https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true)

Problem Statement:
------------------
You will be given a square chess board with one queen and a number of obstacles placed on it.
Determine how many squares the queen can attack.

A queen is standing on an n x n chessboard. The chess board's rows are numbered from 1 to n, going from bottom to top.
Its columns are numbered from 1 to n, going from left to right. Each square is referenced by a tuple,(r, c) , describing the row, r,
and column, c, where the square is located.
The queen is standing at position (rq, cq). In a single move, she can attack any square in any of the eight directions (left, right, up, down, and the four diagonals).

Example:
--------

sample Input #1:
-------------
4 0
4 4

sample output #1:
--------------
9

sample input #2:
----------------
5 3
4 3
5 5
4 2
2 3

sample output #2:
----------------
10

sample input #3:
----------------
1 0
1 1

sample output #3:
-----------------
0

Input format description:
-------------------------
The first line contains two space-separated integers n and k, the length of the board's sides and the number of obstacles.
The next line contains two space-separated integers rq and cq, the queen's row and column position.
Each of the next k lines contains two space-separated integers r[i] and c[i], the row and column position of obstacle[i].


Output format description:
-------------------------
- int: the number of squares the queen can attack

constraints:
-----------
+ 0 < n <= 10 ^ 5
+ 0 <= k <= 10 ^ 5
+ A single cell may contain more than one obstacle.
+ There will never be an obstacle at the position where the queen is located.

Note:
-----

The key of this solution to run in fixed limit is the use of `set` instead of `list`
to store obstacle. the `in` operator run in `O(1)` in average for `set` but in `O(n)` in average for `list`.
For more information, check the link above
[in operator in python](https://note.nkmk.me/en/python-in-basic/#:~:text=source%3A%20in_timeit.py-,Fast%20for%20the%20set%3A%20O(1),on%20the%20number%20of%20elements.&text=The%20execution%20time%20does%20not,the%20value%20to%20look%20for.&text=If%20you%20want%20to%20repeat,to%20a%20set%20in%20advance.)
[time complexity per containers](https://wiki.python.org/moin/TimeComplexity)
"""

import math
import os
import random
import re
import sys
from collections import namedtuple
import dataclasses


def queensAttack(n, k, r_q, c_q, obstacles):
    obstacles = {(r, c) for r, c in obstacles}
    mvs = [
        (1, 0),
        (-1, 0),
        (0, -1),
        (0, 1),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1),
    ]
    count = 0
    for mv in mvs:
        cell_q = (r_q, c_q)

        while check_cell_beglons_to_board(
            next_cell := (cell_q[0] + mv[0], cell_q[1] + mv[1]), n
        ):
            if next_cell in obstacles:
                break

            cell_q = next_cell
            count += 1

    return count


def check_cell_belongs_to_board(cell, board_size):
    return 1 <= cell[0] <= board_size and 1 <= cell[1] <= board_size


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(str(result) + "\n")

    # fptr.close()
