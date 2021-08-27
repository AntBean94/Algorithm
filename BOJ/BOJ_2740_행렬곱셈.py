# BOJ 2740 행렬 곱셈

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

ans = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for s in range(M):
            ans[i][j] += A[i][s] * B[s][j]

for a in ans:
    print(*a)