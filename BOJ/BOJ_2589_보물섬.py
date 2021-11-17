# BOJ 2589 보물섬

'''


'''

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    vis = [[0] * M for _ in range(N)]
    Q = deque()
    Q.append([y, x])
    vis[y][x] = 1
    while Q:
        y, x = Q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == "L":
                if not vis[ny][nx]:
                    vis[ny][nx] = vis[y][x] + 1
                    Q.append([ny, nx])
    return vis[y][x] - 1

ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == "L":
            ans = max(bfs(i, j), ans)
print(ans)