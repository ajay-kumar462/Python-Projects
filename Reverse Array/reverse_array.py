#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'performOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. 2D_INTEGER_ARRAY operations
#

def performOperations(arr, operations):
    # Write your code here
    for each_set in operations:
        first_num = each_set[0]
        second_num = each_set[1]
        new_arr = arr[first_num:second_num+1]
        print(f"array: {arr}")
        print(f"operations: {operations}")
        new_arr.reverse()
        # arr[first_num] = new_arr[0]
        # arr[second_num] = new_arr[1]
        left_arr = arr[:first_num]
        left_arr.append(new_arr)
        left_arr.append(arr[second_num:])
        print(f"result: {left_arr}")

if __name__ == '__main__':
    fptr = open('numbers.txt', 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    operations_rows = int(input().strip())
    operations_columns = int(input().strip())

    operations = []

    for _ in range(operations_rows):
        operations.append(list(map(int, input().rstrip().split())))

    result = performOperations(arr, operations)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
