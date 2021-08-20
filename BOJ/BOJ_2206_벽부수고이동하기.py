# BOJ 2206 벽 부수고 이동하기

'''
풀이방법

[
    [[1,0], [2,0], [5,3], [6,4], [7,4]]
    [[2,0], [3,0], [4,0], [0,0], [8,5]]
    [[0,0], [0,0], [0,0], [0,0], [9,6]]
    [[0,0], [0,0], [0,0], [0,0], [0,10]]
    [[0,0], [0,0], [0,0], [0,0], [0,11]]
    [[0,0], [0,0], [0,0], [0,0], [0,12]]
    [[0,0], [0,0], [0,0], [0,0], [0,13]]
    :
    :
    :
]
3차원 배열 활용


[y, x, k]
범위를 벗어나지 않을 때
4방향 탐색

조건 2개
1. 벽이 아니면서 1 더한값이 목적지 보다 작은 경우
k = k

0 => 0 + 
1 => 1 + 
append

2. 벽인데 현재 k = 0 이면서 1더한값이 k = 1인 목적지보다 작은 경우
k => 1

0 => 1 +
append
'''


import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list() for _ in range(N)]
for i in range(N):
    line = input().rstrip()
    for j in line:
        board[i].append(int(j))
# 우, 하, 좌, 상
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

vis = [list([100000000, 1000000000] for _ in range(M)) for _ in range(N)]

def bfs(y, x, k):
    vis[y][x] = [1, 0]
    Q = deque()
    Q.append([y, x, k])
    while Q:
        t = Q.popleft()
        y, x, k = t[0], t[1], t[2]
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            # 범위 체크
            if 0 <= ny < N and 0 <= nx < M:
                # 조건 1) 벽이 아니면서 1 더한값이 목적지보다 작은 경우
                if not board[ny][nx] and vis[y][x][k] + 1 < vis[ny][nx][k]:
                    vis[ny][nx][k] = vis[y][x][k] + 1
                    Q.append([ny, nx, k])
                # 조건 2) 벽인데 k = 0 이면서 1 더한값이 목적지 (1)보다 작은 경우
                elif board[ny][nx] and k == 0 and vis[y][x][k] + 1 < vis[ny][nx][1]:
                    vis[ny][nx][1] = vis[y][x][k] + 1
                    Q.append([ny, nx, 1])

bfs(0, 0, 0)
ans = min(vis[N - 1][M - 1])
if ans == 100000000:
    print(-1)
elif ans == 0:
    print(1)
else:
    print(ans)