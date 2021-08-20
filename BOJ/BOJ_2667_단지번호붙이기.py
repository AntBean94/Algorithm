# BOJ 2667 단지번호붙이기

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list() for _ in range(N)]
for i in range(N):
    line = input().rstrip()
    for j in line:
        board[i].append(int(j))

# 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 방문 기록
vis = [[0] * N for _ in range(N)]

def bfs(y, x, cnt):
    vis[y][x] = 1
    Q = deque()
    Q.append([y, x])
    while Q:
        t = Q.popleft()
        for d in range(4):
            ny, nx = t[0] + dy[d], t[1] + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if vis[ny][nx] or not board[ny][nx]:
                    continue
                if board[ny][nx] != cnt:
                    board[ny][nx] = cnt
                vis[ny][nx] = 1
                Q.append([ny, nx])
                ans[cnt] += 1

ans = [0] * 100
cnt = 0
for i in range(N):
    for j in range(N):
        if not vis[i][j] and board[i][j]:
            cnt += 1
            ans[cnt] += 1
            board[i][j] = cnt
            bfs(i, j, cnt)


print(cnt)
for i in sorted(ans[1:cnt + 1]):
    print(i)