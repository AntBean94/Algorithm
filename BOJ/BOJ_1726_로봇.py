# BOJ 1726 로봇

'''
vis = [
    [[0, 0, 0, 0], [0, 0, 0, 0], ...]
    [[0, 0, 0, 0], [0, 0, 0, 0], ...]
    [[0, 0, 0, 0], [0, 0, 0, 0], ...]
    [[0, 0, 0, 0], [0, 0, 0, 0], ...]
]

모든 태스크를 1개의 시간으로 분리해야 정확히 측정 가능

'''

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
SY, SX, SD = map(int, input().split())
GY, GX, GD = map(int, input().split())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
trans = [0, 1, 3, 2, 0]
SY, SX, SD = SY - 1, SX - 1, trans[SD]
GY, GX, GD = GY - 1, GX - 1, trans[GD]
rotate = lambda x: [x + 1, x - 1]

def bfs():
    vis = [list([0] * 4 for _ in range(M)) for _ in range(N)]
    Q = deque()
    Q.append([SY, SX, SD])
    vis[SY][SX][SD] = 1
    while Q:
        y, x, d = Q.popleft()
        # 이동
        for i in range(1, 4):
            ny, nx = y + dy[d] * i, x + dx[d] * i
            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx]: break
                if vis[ny][nx][d]: continue
                vis[ny][nx][d] = vis[y][x][d] + 1
                Q.append([ny, nx, d])
        # 회전
        for nd in rotate(d):
            nd %= 4
            if not vis[y][x][nd]:
                vis[y][x][nd] = vis[y][x][d] + 1
                Q.append([y, x, nd])
    print(vis[GY][GX][GD] - 1)
bfs()