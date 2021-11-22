"""
[source](https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true&h_r=next-challenge&h_v=zen)

Problem statement
-----------------
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Examples
--------
+ s = '12:01:00PM'
return ('12:01:00')
+ s = '12:01:00AM'
return ('00:01:00')

Input Format Description
------------------------
A single string s that represents a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM).

Output Format Description
-------------------------
string: the time in 24-hour format

Constraints
-----------
All input times are valid
"""

import math
import os
import random
import re
import sys

def time_conversion(s):
	time_regex = "(?P<hour>\d{2}):(?P<minutes>\d{2}):(?P<seconds>\d{2})(?P<meridiem>[AP]M)"
	hour, minutes, seconds, meridiem = re.match(time_regex, s).groups()
	hour, minutes, seconds = map(int, (hour, minutes, seconds))

	if hour != 12 and meridiem == 'PM':
		hour += 12
	
	if hour == 12 and meridiem == 'AM':
		hour = 0

	hour, minutes, seconds = one_to_two([hour, minutes, seconds])

	result = f"{hour}:{minutes}:{seconds}"

	return result

def one_to_two(numbers):
	for i in range(len(numbers)):
		if len(str(numbers[i])) == 1:
			numbers[i] = f"{0}{numbers[i]}"
		else:
			numbers[i] = f"{numbers[i]}"

	return numbers

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = time_conversion(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
