"""
[source](https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true)

Problem statement
-----------------

HackerLand University has the following grading policy:
+ Every student receives a grade in the inclusive range from 0 to 100.
+ Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:
+ If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
+ If the value of  is less than , no rounding occurs as the result will still be a failing grade.

Examples
--------
+ grade = 84 round to 85 (85 - 84 is less than 3)
+ grade = 29 do not round (result is less than 40)
+ grade = 57 do not round (60 - 57 is 3 or higher)

Given the initial value of  for each of Sam's  students, write code to automate the rounding process.

Input Format Description
------------------------
The first line contains a single integer,n , the number of students.
Each line i of the n subsequent lines contains a single integer, gradles[i].

Output Format Description
-------------------------
int[n]: the grades after rounding as appropriate

Constraints
-----------
+ 1 <= n <= 60
+ 0 <= grades[i] <= 100
"""

import math
import os
import random
import re
import sys


def grading_students(grades):
    result = map(_round, grades)
    return result


def _round(grade):
    if grade < 38:
        return grade
    next_multi = math.ceil(grade / 5) * 5
    return next_multi if next_multi - grade < 3 else grade


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = grading_students(grades)

    print("\n".join(map(str, result)))
    # fptr.write("\n".join(map(str, result)))
    # fptr.write("\n")
    # fptr.close()
