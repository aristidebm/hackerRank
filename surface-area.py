"""
[source](https://www.hackerrank.com/challenges/3d-surface-area/problem?isFullScreen=true)

Algorithm :

Pour une matrice A d'ordre M x N.

1. La face basse contient M x N elements.
2. La face haute continent M x N elements.
3. Pour chaque cellule il faut calculer le nombre de face visible partie les quatres faces restantes.
    Le nombre de faces visibles parmi celles restantes est obtenu par l'agorithme suivant
    Soit (i, j) la cellule en cours.
    
    + Definir un compteur "c"
    + Enumerer ses cellules adjancentes S = {(i, j + 1), (i, j-1), (i-1, j), (i + 1, j)}
    + Pour chaque a in S.
    + Si a n'existe pas (pas une cellule du tableau)
        - c += Aij
    + Si a existe et Aa < Aij
        - c += Aij - Aa // on peut juste utiliser la fonction max(Aij - Aa, 0)
    + Le "c" est le nombre de face visibles de la cellule (i, j). 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#


def surfaceArea(A):
    # Write your code here

    M = len(A)
    N = len(A[0])

    # bottom and top side.
    surface = 2 * M * N

    for i in range(M):
        for j in range(N):
            if in_grid(A, i, j - 1):
                surface += max(A[i][j] - A[i][j - 1], 0)
            else:
                surface += A[i][j]

            if in_grid(A, i, j + 1):
                surface += max(A[i][j] - A[i][j + 1], 0)
            else:
                surface += A[i][j]

            if in_grid(A, i - 1, j):
                surface += max(A[i][j] - A[i - 1][j], 0)
            else:
                surface += A[i][j]

            if in_grid(A, i + 1, j):
                surface += max(A[i][j] - A[i + 1][j], 0)
            else:
                surface += A[i][j]

    return surface


def in_grid(A, i, j):
    return 0 <= i < len(A) and 0 <= j < len(A[0])


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    print(str(result) + "\n")
