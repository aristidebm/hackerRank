# [source](https://www.hackerrank.com/challenges/two-pluses/problem?isFullScreen=true)

# A pretty goog explanation can be found here https://www.youtube.com/watch?v=COYqFbIAAOs

# Remarques :
# ----------
# 1. Le croix d'aires egale a 1 ne nous interessent pas, elle n'apporte aucune information au calcul d'aire.
# 2. Toutes les croix valides on une aire de la forme A = 2 ^ n + 1 avec n un entier naturel.
# 3. Pour ces croix, la cellule du milieu ne peut se trouver ni sur la premiere ligne, ni sur la derniere ligne
# ni sur la premiere colonne, ni sur la derniere colonne.
#
# Algorithm
# ---------
# Well Explained here https://www.youtube.com/watch?v=COYqFbIAAOs
# 0. Initialize the area to 0
# 1. Find the plus and colorized it (in the code, the color is *)
# 2. Keeping the above plus colorized, loop through the grid to find the second plus that does not overlap with above
# 3. Compute the product of the two found pluses and compute the area as
# area = (area, first_plus_area * second_plus_area)
# 4. Go to step 1 and find another valid plus and repeat the process.

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce


class Solution:
    def tow_pluses(self, grid):
        R = len(grid)
        C = len(grid[0])
        area = 0
        # add border to avoid array index error
        grid = self.add_border(grid)
        self.print_grid(grid)
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                offset = 0
                while (
                    grid[i - offset][j] == "G"
                    and grid[i + offset][j] == "G"
                    and grid[i][j - offset] == "G"
                    and grid[i][j + offset] == "G"
                ):
                    # mark the plus as already used
                    grid[i - offset][j] = grid[i + offset][j] = grid[i][
                        j - offset
                    ] = grid[i][j + offset] = "*"

                    self.print_grid(grid)

                    for y in range(1, R + 1):
                        for x in range(1, C + 1):
                            new_offset = 0
                            while (
                                grid[y - new_offset][x] == "G"
                                and grid[y + new_offset][x] == "G"
                                and grid[y][x - new_offset] == "G"
                                and grid[y][x + new_offset] == "G"
                            ):
                                # mark the plus as already used
                                area = max(
                                    area, (4 * offset + 1) * (4 * new_offset + 1)
                                )
                                new_offset += 1

                    offset += 1

                self.reset_board(i, j, grid)

        return area

    def add_border(self, grid):
        R = len(grid)
        C = len(grid[0])
        temp = [["O"] * (C + 2)]

        for i in range(R):
            temp.append(["O"] + list(grid[i]) + ["O"])
        temp.append(["O"] * (C + 2))

        return temp

    def reset_board(self, i, j, grid):
        r = 0
        while (
            grid[i - r][j] == "*"
            and grid[i + r][j] == "*"
            and grid[i][j - r] == "*"
            and grid[i][j + r] == "*"
        ):
            # mark the plus as already used
            grid[i - r][j] = grid[i + r][j] = grid[i][j - r] = grid[i][j + r] = "G"
            r += 1

        return grid

    def print_grid(self, grid):
        for row in grid:
            print(*row)
        print()


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = Solution().tow_pluses(grid)

    print(result)

# 5 6
# GGGGGG
# GBBBGB
# GGGGGG
# GBGGGG
# BGBGBG

# 5 6
# GGGGGG
# GGGGGG
# GGGGGG
# GGGGGG
# GGGGGG

# 6 6
# BGBBGB
# GGGGGG
# BGBBGB
# GGGGGG
# BGBBGB
# BGBBGB
