"""
[source](https://www.hackerrank.com/challenges/bon-appetit/problem?h_r=next-challenge&h_v=zen)

Problem statement:
------------------
Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill = [2, 4, 6]
. Anna declines to eat item k = bill[2] which costs 6. If Brian calculates the bill correctly, Anna will pay (2 + 4)/2 = 3. If he includes the cost of bill[2], he will calculate (2 + 4 + 6)/2 = 6. In the second case, he should refund to Anna.

Example:
--------
4 1
3 10 2 9
12

5

4 1
3 10 2 9
7

Bon Appetit

Input format description:
-------------------------
+ The first line contains two space-separated integers and n, k the number of items ordered and the 0-based index of the item that Anna did not eat.

+ The second line contains n space-separated integers bill[i] where 0 <= i <= n.
The third line contains an integer, , the amount of money that Brian charged Anna for her share of the bill

+ The third line contains an integer, b, the amount of money that Brian charged Anna for her share of the bill.

Output format description:
--------------------------
If Brian did not overcharge Anna, print Bon Appetit on a new line; otherwise, print the difference (i.e., b_charged - b_actual) that Brian must refund to Anna. This will always be an integer.

constraints
-----------
+ 2 <= n <= 10 ^ 5
+ 0 <= k < n
+ 0 <= bill[i] <= 10^4
+ 0 <= b <= sum_{i = 0}^{n - 1}bill[i]
+ The amount of money due Anna will always be an integer.
"""

import math
import os
import random
import re
import sys


def bon_appetit(bill, k, b):
    correct = sum(bill[i] for i in range(len(bill)) if i != k) / 2
    if correct != b:
        print(f"{b - correct:.0f}")
        return

    print("Bon Appetit")


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bon_appetit(bill, k, b)
