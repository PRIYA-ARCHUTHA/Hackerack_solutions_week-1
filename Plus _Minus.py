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
    total = len (arr)
    
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    for num in arr :
        if num >0:
            positive_count+=1
        elif num<0:
            negative_count+=1
        else :
             zero_count+=1
    #condition
    positive_sum = positive_count/total
    negative_sum = negative_count/total
    zero_sum = zero_count/total
    
    print(f"{positive_sum :.6f}")
    print(f"{negative_sum:.6f}")
    print(f"{zero_sum:.6f}")

   

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
