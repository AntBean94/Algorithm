# BOJ 2146 다리 만들기

'''
방문 기록
거리, 지역
[1, (1, 2, 3, ...)]

섬을 간척하며 최단거리 측정(bfs)
'''

from collections import deque
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x, n):
    Q = deque()
    Q.append([y, x])
    vis[y][x] = [1, n]
    while Q:
        y, x = Q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] == 1 and not vis[ny][nx][0]:
                    vis[ny][nx] = [1, n]
                    Q.append([ny, nx])
# 섬 나누기
vis = [[[0, 0] for _ in range(N)] for _ in range(N)]
num = 1
for i in range(N):
    for j in range(N):
        if board[i][j] and not vis[i][j][0]:
            bfs(i, j, num)
            num += 1

def reclaim(y, x, dis):
    now = vis[y][x][1]
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if not (0 <= ny < N and 0 <= nx < N): continue
        # 방문 흔적이 없다면 간척
        if not vis[ny][nx][0]:
            vis[ny][nx] = [dis + 1, now]
        # 방문 흔적이 있는데 다른 섬
        elif vis[ny][nx][0] and vis[ny][nx][1] != now:
            return False, dis + vis[ny][nx][0] - 2
    return True, 0

# 간척
min_dis = 1000000
dis = 1
check = True
while check:
    for i in range(N):
        for j in range(N):
            if vis[i][j][0] == dis:
                # 함수
                sig, result = reclaim(i, j, dis)
                if not sig:
                    min_dis = min(result, min_dis)
                    check = False
    dis += 1

print(min_dis)