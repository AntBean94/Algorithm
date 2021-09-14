# BOJ 15652 N과 M (4)

import sys

N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
tmp = []

def back_t(arr, m, i):
    if m == M:
        sys.stdout.writelines(" ".join(map(str, tmp)) + '\n')
        return
    for j in range(i, N):
        tmp.append(arr[j])
        back_t(arr, m + 1, j)
        tmp.pop()

back_t(arr, 0, 0)