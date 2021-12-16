# BOJ 4963 섬의 개수

'''

'''

from collections import deque

# 상, 우, 하, 좌, 우상, 우하, 좌하, 좌상
dy = [-1, 0, 1, 0, -1, 1, 1, -1]
dx = [0, 1, 0, -1, 1, 1, -1, -1]

def bfs(y, x):
    vis[y][x] = 1
    Q = deque()
    Q.append([y, x])
    while Q:
        y, x = Q.popleft()
        for d in range(8):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < H and 0 <= nx < W:
                if not vis[ny][nx] and board[ny][nx]:
                    Q.append([ny, nx])
                    vis[ny][nx] = 1
    return

while True:
    W, H = map(int, input().split())
    # 종료 조건
    if not W: break
    # 지도 정보 입력
    board = [list(map(int, input().split())) for _ in range(H)]
    # 방문 기록
    vis = [[0] * W for _ in range(H)]
    cnt = 0
    # 순회
    for i in range(H):
        for j in range(W):
            if not vis[i][j] and board[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)