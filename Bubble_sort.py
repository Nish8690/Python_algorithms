import math
import os
import random
import re
import sys
# 3
# 1 2 3

# Complete the countSwaps function below.
def countSwaps(a, n):
    count = 0
    for i in range(n):
        for j in range(1, n - i):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                count += 1
    print('Array is sorted in', count, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a, n)
