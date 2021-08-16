# 계수 정렬 (Counting Sort) 예제

import sys 

arr = [1, 3, 2, 4, 1, 3, 2, 2, 5, 4, 2, 3, 4, 1, 5, 5, 1]
rng = 5     # 범위

def CountingSort(arr, n):
    cnt_arr = [0] * n
    for a in arr:
        cnt_arr[a - 1] += 1
    print(cnt_arr)
    for i in range(n):
        num = i + 1
        for _ in range(cnt_arr[i]):
            sys.stdout.write("%d " %num)

CountingSort(arr, rng)