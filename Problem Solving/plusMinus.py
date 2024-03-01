#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code
    count_negative = 0
    count_zero = 0
    count_positive = 0
    for i in range(0, len(arr)):
        if arr[i] < 0:
            count_negative = count_negative + 1
        elif arr[i] == 0:
            count_zero = count_zero + 1
        elif arr[i] > 0:
            count_positive = count_positive + 1
    negative_rate = "{:.6f}".format(float(count_negative / len(arr)))
    positive_rate = "{:.6f}".format(float(count_positive / len(arr)))
    zero_rate = "{:.6f}".format(float(count_zero / len(arr)))

    print(positive_rate)
    print(negative_rate)
    print(zero_rate)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
