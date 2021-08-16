# 버블정렬(Bubble Sort) 에제

import sys

arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(len(arr)-1):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

sys.stdout.write(" ".join(map(str, arr)))