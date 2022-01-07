# BOJ 1890 점프

'''
Nij = sum(possible N-1ij)
'''

import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]
# 초기화
DP[0][0] = 1
for i in range(N):
    for j in range(N):
        n = board[i][j]
        if not n: continue
        # 이동할 좌표
        nr, nd = j + n, i + n
        if 0 <= nr < N: DP[i][nr] += DP[i][j]
        if 0 <= nd < N: DP[nd][j] += DP[i][j]
print(DP[-1][-1])