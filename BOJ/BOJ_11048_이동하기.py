# BOJ

'''
우, 하, 우하 이동가능

점화식
DP[i][j] = max(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + Aij
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if 0 <= i - 1 < N and 0 <= j - 1 < M: leftup = DP[i-1][j-1]
        else: leftup = 0
        if 0 <= i - 1 < N and 0 <= j < M: up = DP[i-1][j]
        else: up = 0
        if 0 <= i < N and 0 <= j - 1 < M: left = DP[i][j-1]
        else: left = 0
        DP[i][j] = max(leftup, up, left) + A[i][j]

print(DP[N-1][M-1])