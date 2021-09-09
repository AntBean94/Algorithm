# BOJ 11049 행렬 곱셈 순서

'''
연쇄 행렬 곱

구간 테이블에 값을 기록

점화식 DP[i][j] = min(DP[i][k] + DP[k+1][j] + mul) (i <= k < j)
mul = A[i][k] * A[k+1][j] 의 연산 횟수(행렬)
'''

import sys
input = sys.stdin.readline

INF = 10000000000
N = int(input())
matrix = [0] + [list(map(int, input().split())) for _ in range(N)]
cum = []
for i in range(N):
    matrix[i + 1]
DP = [[0] * (N + 1) for _ in range(N + 1)]

for d in range(1, N):
    for l in range(1, N - d + 1):
        r = l + d
        DP[l][r] = INF
        for k in range(l, r):
            mul = matrix[l][0] * matrix[k][1] * matrix[r][1]
            DP[l][r] = min(DP[l][r], DP[l][k] + DP[k+1][r] + mul)
print(DP[1][N])