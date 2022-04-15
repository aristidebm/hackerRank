"""
[source](https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true)

Problem statement:
-----------------
We define a magic square to be an n x n matrix of distinct positive integers from 1 to n ^ 2 where
the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.
You will be given a 3 x 3 matrix s of integers in the inclusive range [1, 9]. We can convert any digit a to any
other digit b in the range [0-9] at cost of |a - b|. Given s, convert it into a magic square at minimal cost.
Print this cost on a new line.

# NOTE: The resulting magic square must contain distinct integers in the inclusive range.

Example:
--------
5 3 4
1 5 8
6 4 2

We can convert it to the following magic square:

8 3 4
1 5 9
6 7 2

This took three replacements at a cost of: | 5 - 8 | + | 8 - 9 | + | 4 - 7 | = 7.

Input Format Description:
-------------------------
Each of the 3 lines contains three space-separated integers of row s[i].

Output Format Description:
--------------------------
+ int: the minimal total cost of converting the input square to a magic square

Constraints:
------------
+ s[i][j] in [0 - 9]

The 8 valid combinations of 3 numbers that add to 15 are:
"""

from functools import wraps
import logging
import sys

magic_constant = 15

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def description(desc=None):
    def wrapper(func):
        @wraps(func)
        def wrappee(cls, *args, **kwargs):
            return func(cls, *args, **kwargs)

        wrappee.description = desc or ""
        return wrappee

    return wrapper


class Transformation:
    @classmethod
    @description("Initial Square Matrix")
    def rotate_360(cls, matrix):
        return matrix

    @classmethod
    @description("Rotation of angle 90")
    def rotate_90(cls, matrix):
        return list(zip(*matrix))

    @classmethod
    @description("Horizontal reflection")
    def horizontal_axial_symmetry(cls, matrix):
        return matrix[::-1]

    @classmethod
    @description("Vertical reflection")
    def vertical_axial_symmetry(cls, matrix):
        return [matrix[r][::-1] for r in range(len(matrix))]

    @classmethod
    @description("Vertical reflection --> Horizontal reflection")
    def vertical_axial_horizontal_axial_symmetry(cls, matrix):
        return cls.horizontal_axial_symmetry(cls.vertical_axial_symmetry(matrix))

    @classmethod
    @description("Rotation of angle 90 --> Horizontal reflection")
    def rotate_90_horizontal_symmetry(cls, matrix):
        return cls.horizontal_axial_symmetry(cls.rotate_90(matrix))

    @classmethod
    @description("Rotation of angle 90 --> Vertical reflection")
    def rotate_90_vertical_axial_symmetry(cls, matrix):
        return cls.vertical_axial_symmetry(cls.rotate_90(matrix))

    @classmethod
    @description(
        "Rotation of angle 90 --> Vertical reflection --> Horizontal reflection"
    )
    def rotate_90_vertical_axial_horizontal_axial_symmetry(cls, matrix):
        return cls.vertical_axial_horizontal_axial_symmetry(cls.rotate_90(matrix))


def is_magic_square(matrix):
    predicate = []

    # Check rows sum
    for row in matrix:
        predicate.append(sum(row) == magic_constant)

    # Check columns
    for col in zip(*matrix):
        predicate.append(sum(row) == magic_constant)

    # Check diagonal sums
    predicate.append(sum(matrix[i][i] for i in range(len(matrix))) == magic_constant)

    # Check second diagonal sums
    predicate.append(
        sum(matrix[i][len(matrix) - i - 1] for i in range(len(matrix)))
        == magic_constant
    )

    return all(predicate)


def compute_cost(origin, sq_matrix):
    return sum(
        abs(i - j)
        for o_row, sq_row in zip(origin, sq_matrix)
        for i, j in zip(o_row, sq_row)
    )


def pretty_print_matrix(matrix):
    content = []
    content.append(" " + "-" * (len(matrix) + 8))
    for row in matrix:
        content.append(f"| {' | '.join(map(str,row))} |")
        content.append(" " + "-" * ((len(matrix) + 8)))

    return "\n".join(content)


def debug(sq_matrix, cost, transfo):
    return f"\n{pretty_print_matrix(sq_matrix)}\n\nCost : {cost}\nMagic square ? : {is_magic_square(sq_matrix)}\nTransformation: {transfo.description}\n"


def forming_magic_square(matrix):
    if is_magic_square(matrix):
        # Nothing to do since the provided matrix is already a magic square.
        return 0

    temp_matrix = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]

    transformations = [
        getattr(Transformation, f)
        for f in dir(Transformation)
        if not f.startswith("__")
    ]
    min_cost = float("inf")

    for transfo in transformations:
        sq_matrix = transfo(temp_matrix)
        cost = compute_cost(matrix, sq_matrix)
        min_cost = min(min_cost, cost)
        logger.debug(debug(sq_matrix, cost, transfo))

    return min_cost


def main():
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = forming_magic_square(s)

    print("\nLowest Cost : " + str(result) + "\n")


if __name__ == "__main__":
    level = None
    if len(sys.argv) > 1:
        level = sys.argv[1]
        logger.level = int(level)

    main()
