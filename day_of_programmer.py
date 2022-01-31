"""
[source](https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true)

Problem statement:
------------------
Marie invented a Time Machine and wants to test it by time-traveling to visit Russia on the Day of the Programmer (the 256th day of the year) during a year in the inclusive range from 1700 to 2700.

From 1700 to 1917, Russia's official calendar was the Julian calendar; since 1919 they used the Gregorian calendar system. The transition from the Julian to Gregorian calendar system occurred in 1918, when the next day after January 31st was February 14th. This means that in 1918, February 14th was the 32nd day of the year in Russia.

In both calendar systems, February is the only month with a variable amount of days; it has 29 days during a leap year, and 28 days during all other years. In the Julian calendar, leap years are divisible by 4; in the Gregorian calendar, leap years are either of the following:

    + Divisible by 400.
    + Divisible by 4 and not divisible by 100.

Given a year, [y], find the date of the 256th day of that year according to the official Russian calendar during that year. Then print it in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is [y].

Example:
--------
For example, the given year = 1984. 1984 is divisible by 4, so it is a leap year. The 256th day of a leap year after 1918 is September 12, so the answer is 12.09.1984. 

Input format description:
-------------------------
A single integer denoting year y.

Output format description:
--------------------------
Print the full date of Day of the Programmer during year [y] in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is [y].

constraints
-----------
1700 <= year <= 2700
"""
import math
import os
import random
import re
import sys
from datetime import datetime

duration_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_julian_leap_year(year):
    # return (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)
    # In julian calendar, a leap year is a year that is divisible by 4
    return year % 4 == 0


def gregrorian(year: int, day: int):
    return datetime.strptime(f"{year}-{day}", "%Y-%j").strftime("%d.%m.%Y")


def _find_julian_day(year: int, day: int):

    cp = duration_of_month.copy()

    # In 1918 the next day after January 31st was February 14th and 1918 is not leap
    # so February duration for that year is 14.
    if year == 1918:
        cp[1] = 14

    if is_julian_leap_year(year):
        cp[1] = 29

    month_y, s = 0, 0
    for m_duration in cp:
        if s + m_duration < day:
            month_y += 1
            s += m_duration

    day_y = day - sum(cp[:month_y] or [0])
    month_y += 1
    month_y = month_y if month_y > 9 else f"{0}{month_y}"
    return f"{day_y}.{month_y}.{year}"


def julian(year: int, day: int):
    return _find_julian_day(year, day)


def _decide_calendar_system(year):
    return gregrorian if 1918 < year <= 2700 else julian


def day_of_programmer(year: int, day: int = None) -> str:
    day = day or 256
    return _decide_calendar_system(year)(year, day)


if __name__ == "__main__":
    year = int(input().strip())
    result = day_of_programmer(year)
    print(result + "\n")
