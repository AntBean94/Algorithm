# BOJ 7576 토마토

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
start = []
board = [list() for _ in range(N)]
for i in range(N):
    cnt = 0
    for j in map(int, input().split()):
        if j == 1: start.append([i, cnt])
        board[i].append(j)
        cnt += 1


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

vis = [[0] * M for _ in range(N)]

dist = {}

def bfs(start):
    Q = deque()
    for s in start:
        Q.append(s)
        vis[s[0]][s[1]] = 1
    while Q:
        t = Q.popleft()
        for d in range(4):
            ny, nx = t[0] + dy[d], t[1] + dx[d]
            if 0 <= ny < N and 0 <= nx < M:
                if not vis[ny][nx] and not board[ny][nx]:
                    board[ny][nx] = 1
                    vis[ny][nx] = vis[t[0]][t[1]] + 1
                    Q.append([ny, nx])
                    dist[vis[ny][nx]] = 1

bfs(start)
for i in range(N):
    for j in range(M):
        if not board[i][j]:
            print(-1)
            exit()

if dist:
    print(max(dist.keys()) - 1)
else:
    print(0)