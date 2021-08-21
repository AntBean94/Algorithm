# BOJ 7562 나이트의 이동

import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs(start, end, vis):
    y, x = start[0], start[1]
    vis[y][x] = 1
    Q = deque()
    Q.append(start)
    while Q:
        y, x = Q.popleft()
        for d in range(8):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < I and 0 <= nx < I:
                if not vis[ny][nx]:
                    vis[ny][nx] = vis[y][x] + 1
                    Q.append([ny, nx])
                    if ny == end[0] and nx == end[1]:
                        print(vis[ny][nx] - 1)
                        Q = []
                        break

T = int(input())

for tc in range(T):
    I = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    if start == end:
        print(0)
        continue
    vis = [[0] * I for _ in range(I)]
    bfs(start, end, vis)