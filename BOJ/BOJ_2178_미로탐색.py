# BOJ 2178 미로 탐색

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list() for _ in range(N)]
for i in range(N):
    line = input().rstrip()
    for j in line:
        board[i].append(int(j))

vis = [[0] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(y, x):
    vis[y][x] = 1
    Q = deque()
    Q.append([y, x])
    while Q:
        t = Q.popleft()
        for d in range(4):
            ny, nx = t[0] + dy[d], t[1] + dx[d]
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx]:
                if not vis[ny][nx]:
                    vis[ny][nx] = vis[t[0]][t[1]] + 1
                    Q.append([ny, nx])

bfs(0, 0)
print(vis[N - 1][M - 1])