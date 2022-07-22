# [source](https://www.hackerrank.com/challenges/two-pluses/problem?isFullScreen=true)

# Algorithm
# ---------

# Well Explained here https://www.youtube.com/watch?v=COYqFbIAAOs
# The approach is a greedy approach, we can't do better than that, though we have to check all valid pluses of grid

# 0. Initialize the area to 0
# 1. Begin with plus (A) with area 1 if exists, mark the plus as visited.
# 2. Keeping the above plus mark as visited, Loop through the grid to find respectively a plus with area 1, 5, ..., 4n + 1
# 3. For Each plus in above, compare area with product (area(A) * 4*n + 1) and take the maximum each time.
# 4. Change the Grid to it's initial state (by umarking the plus with area 1)
# 5. Iteratively find the pluses of area 5, 9, ..., 4*n + 1 and for each plus mark them as visited and repeat the steps
# 2 to 4.

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

# samples

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
