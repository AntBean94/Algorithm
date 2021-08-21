# BOJ 7569 토마토 3D

import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
start = []
board = [list(list() for _ in range(N)) for _ in range(H)]
for h in range(H):
    for i in range(N):
        cnt = 0
        for j in map(int, input().split()):
            if j == 1: start.append([h, i, cnt])
            board[h][i].append(j)
            cnt += 1

dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 0, 1, 0]
dx = [0, 0, 0, -1, 0, 1]

vis = [list([0] * M for _ in range(N)) for _ in range(H)]

dist = {}

def bfs(start):
    Q = deque()
    for s in start:
        Q.append(s)
        vis[s[0]][s[1]][s[2]] = 1
    while Q:
        t = Q.popleft()
        for d in range(6):
            nh, ny, nx = t[0] + dz[d], t[1] + dy[d], t[2] + dx[d]
            if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M:
                if not vis[nh][ny][nx] and not board[nh][ny][nx]:
                    board[nh][ny][nx] = 1
                    vis[nh][ny][nx] = vis[t[0]][t[1]][t[2]] + 1
                    Q.append([nh, ny, nx])
                    dist[vis[nh][ny][nx]] = 1

bfs(start)
for h in range(H):
    for i in range(N):
        for j in range(M):
            if not board[h][i][j]:
                print(-1)
                exit()

if dist:
    print(max(dist.keys()) - 1)
else:
    print(0)