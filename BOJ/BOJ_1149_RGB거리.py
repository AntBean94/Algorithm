# BOJ 1149 RGB거리

import sys
input = sys.stdin.readline

N = int(input())
val = [list(map(int, input().split())) for _ in range(N)]
arr = [[0] * 3 for _ in range(N)]
for i in range(N):
    if i == 0:
        for j in range(3):
            arr[i][j] = val[i][j]
    else:
        for j in range(3):
            for k in range(3):
                if j != k:
                    if not arr[i][j]:
                        arr[i][j] = arr[i - 1][k] + val[i][j]
                    elif arr[i - 1][k] + val[i][j] < arr[i][j]:
                        arr[i][j] = arr[i - 1][k] + val[i][j]
print(min(arr[N-1]))