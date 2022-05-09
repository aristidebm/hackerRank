"""
[source](https://www.hackerrank.com/challenges/bomber-man/problem?isFullScreen=true)

Exemple:
r = 2, c = 2, n = 5

+ Initial
+---+---+
|   |   |
+---+---+
|   | O |
+---+---+

+ 1 sec
+---+---+
|   |   |
+---+---+
|   | O |
+---+---+

+ 2 sec
+---+---+
| O | O |
+---+---+
| O | O |
+---+---+


+ 3 sec
+---+---+
| O |   |
+---+---+
|   |   |
+---+---+

+ 4 sec
+---+---+
| O | O |
+---+---+
| O | O |
+---+---+

+ 5 sec
+---+---+
|   |   |
+---+---+
|   | O |
+---+---+

+ 6 sec
+---+---+
| O | O |
+---+---+
| O | O |
+---+---+

+ 7 sec
+---+---+
| 0 |   |
+---+---+
|   |   |
+---+---+

Algorithm :
+ Si n = 1 ==> Renvoyez le tableau tel qu'il est.
+ Si n % 2 = 0 ==> Renvoyez u tableau rempli de bombes.
+ sinon :
    Repeter les suivantes en parcourant les nombres impaires de [|3, n|]
    1. Recuperer les positions des bombes dans la grille courante.
    2. Netoyer (mettre la cellule a ".") toutes les solutions (i, j) [position] d'une bombe et les cellules
    en position (i - 1, j), (i + 1, j), (i, j - 1) et (i, j + 1)

Optimisation:
------------
En regardant bien les examples ci-dessus, on remarque un pattern qui se degage pour les n impaires.
+ Le tableau quand n = 1 est le meme que quand n = 5
+ Le tableau quand n = 3 est le meme que quand n = 7
    (7 - 1) / 2 => nombre impaire
    (3 - 1) / 2 => nombre impaire
    (1 - 1) / 2 => nombre paire
    (5 - 1) / 2 => nombre paire

On peut donc dire optimiser l'argorithme en remarquant que
+ (n - 1) / 2 => nombre paire  <=> configuration initial
+ (n - 1) / 2 => nombre impaire <=> configuration full - configuration initial (complementaire de configuration initial)
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#


def bomberMan(n, grid):  # pass all tests

    if n == 1:
        return grid

    if n % 2 == 0:
        return [r.replace(".", "O") for r in grid]

    thirdGrid = explodeBomb(grid)
    fithGrid = explodeBomb(thirdGrid)
    return fithGrid if ((n - 1) / 2) % 2 == 0 else thirdGrid


def explodeBomb(grid):
    # The new grid is the full grid except cell where bombs and their neighbors are located
    R = len(grid)
    C = len(grid[0])

    neighbours = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
    transformedGrid = [list(r) for r in grid]
    fullGird = [["O"] * C for _ in range(R)]

    bombs = locateBomb(transformedGrid)
    # printGrid(grid, b="Initial")

    for b in bombs:
        for n in neighbours:
            if 0 <= b[0] + n[0] < R and 0 <= b[1] + n[1] < C:
                fullGird[b[0] + n[0]][b[1] + n[1]] = "."

        # printGrid(fullGird, b)

    return ["".join(r) for r in fullGird]


def printGrid(grid, b=None):
    if b:
        print(b)
    for r in grid:
        print("".join(r))
    print("\n")


def locateBomb(grid):
    locations = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                locations.append((i, j))
    return locations


# version 1 : # Failed for time limit exceed

# def bomberMan(n, grid):

#     if n == 1:
#         return grid

#     if n % 2 == 0:
#         return fullGrid(grid)

#     counter = 3
#     currentGrid = transformGrid(grid)

#     while counter <= n:
#         if counter % 2 == 0:
#             continue

#         currentGrid = getNextGrid(currentGrid)
#         counter += 1

#     for i in range(len(grid)):
#         currentGrid[i] = "".join(currentGrid[i])

#     return currentGrid

# def getNextGrid(currentGrid):
#     # The new grid is the full grid except cell where bombs and their neighbors are located
#     neighbours = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
#     bombs = locateBomb(currentGrid)
#     nextGrid = fullGrid(currentGrid)

#     for b in bombs:
#         for n in neighbours:
#             if 0 <= b[0] + n[0] < len(currentGrid) and 0 <= b[1] + n[1] < len(
#                 currentGrid[0]
#             ):
#                 nextGrid[b[0] + n[0]][b[1] + n[1]] = "."
#     return nextGrid


# def fullGrid(grid):
#     for i in range(len(grid)):
#         grid[i] = ["O"] * len(grid[0])
#     return grid


# def locateBomb(grid):
#     locations = []
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == "O":
#                 locations.append((i, j))
#     return locations


# def transformGrid(grid):
#     for i in range(len(grid)):
#         grid[i] = list(grid[i])
#     return grid

if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)
    print("\n")
    print("\n".join(result))
    print("\n")
