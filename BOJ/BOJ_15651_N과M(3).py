# BOJ N과 M (3)

import sys

N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
tmp = []

def back_t(arr, m):
    if m == M: 
        sys.stdout.writelines(" ".join(map(str, tmp)) + '\n')
        return
    for a in arr:
        tmp.append(a)
        back_t(arr, m + 1)
        tmp.pop()

back_t(arr, 0)