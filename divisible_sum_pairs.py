"""
[source](https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true)

Problem statement
-----------------
Given an array of integers and a positive integer k, determine the number of (i, j) pairs where i < j and  arr[i] + arr[j] is divisible by k.

Examples
--------
arr = [1, 2, 3, 4, 5, 6]
k = 5

Three pairs meet the criteria: [1, 4], [2, 3], and [4, 6]

Input Format Description
------------------------
The first line contains  space-separated integers, n and k .
The second line contains n space-separated integers, each a value of arr[i].

Output Format Description
-------------------------
int: the number of pairs

constraints
-----------
+ 2 <= n <= 100
+ 1 <= k <= 100
+ 1 <= arr[i] <= 100
"""


def divisible_sum_pairs(n, k, arr):
    # Write your code here
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j]) % k == 0:
                count += 1
    return count


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisible_sum_pairs(n, k, ar)

    print(str(result) + "\n")
    # fptr.write(str(result) + '\n')

    # fptr.close()
