# [source](https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true&h_r=next-challenge&h_v=zen)

"""
A pretty simple and elegant solution found in discussion board.

1. prendre le premier caractere, faire un pas du nombre de colonne ainsi de suite jusqu'a atteindre la fin de la chaine.
2. prendre le second caractere, faire un pas du nombre de colonne ainsi de suite jusqu'a atteindre la fin de la chaine.
3. continue le processus jusqu'a ce qu'on ne (nombre de colonne)-ieme caractere.

import math

sm=s.replace(" ","")
r=math.floor(math.sqrt(len(sm)))
c=math.ceil(math.sqrt(len(sm)))

for i in range(c):
    print(sm[i::c],end=" ")

"""

import math


def encryption(s):
    # find row and column
    s = s.replace(" ", "")
    L = len(s)
    row = math.floor(math.sqrt(L))
    col = math.ceil(math.sqrt(L))

    row = row if row * col >= L else row + 1

    # reshape the string and store it in a grid.
    grid = [s[i * col : (i + 1) * col] for i in range(row)]

    result = []
    for i in range(col):
        cols = []
        for r in grid:
            try:
                cols.append(r[i])
            except IndexError:
                continue

        result.append("".join(cols))

    return " ".join(result)


if __name__ == "__main__":

    s = input()

    result = encryption(s)

    print(result + "\n")

# Example:
# if man was meant to stay on the ground god would have given us roots
# haveaniceday
