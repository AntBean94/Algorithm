# 삽입 정렬(Insertion Sort) 예제

import sys

arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(1, len(arr)):
    for j in range(i-1, -1, -1):
        if arr[j+1] < arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
        else:
            break

sys.stdout.write(" ".join(map(str, arr)) + '\n')
