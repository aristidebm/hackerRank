"""
[source](https://www.educative.io/courses/grokking-the-coding-interview/Smallest_Subarray_With_a_Greater_Sum_easy_Grokking_the_Coding_Interview.html)

Problem Statement:
------------------
Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

Example:
--------

>>> numbers = [2, 1, 5, 2, 3, 2]
>>> S = 7
2

>>> numbers = [2, 1, 5, 2, 8]
>>> S = 8
1

>>> numbers = [3, 4, 1, 1, 6]
>>> S = 8
3

Input Format Description:
-------------------------

+ An array of numbers `numbers`
+ A target Integer

Output Format Description:
--------------------------
+ An integer that designate the size of the smallest subset with maximun sum.

"""


def main():
    numbers = [2, 1, 5, 2, 8]
    target = 8
    print(find_length(numbers, target))


def find_length(numbers, target):

    length = 0

    for idx in range(len(numbers)):

        curr_sum, curr_len = numbers[idx], 1

        if curr_sum >= target:
            return curr_len

        for item in numbers[idx + 1 :]:

            curr_len += 1

            if curr_sum + item >= target:
                length = min(curr_len, length) if length != 0 else curr_len
                break
            else:
                curr_sum += item

    return length


if __name__ == "__main__":
    main()
