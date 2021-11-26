# BOJ 6087 레이저 통신

'''
거리제한이 없는 bfs
'''

from collections import deque

W, H = map(int, input().split())
board = [list() for _ in range(H)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
start = []
end = []
for i in range(H):
    info = input()
    for j in range(W):
        if info[j] == "C":
            if start: end = [i, j]
            else: start = [i, j]
        board[i].append(info[j])

def bfs(y, x):
    vis = [[0] * W for _ in range(H)]
    Q = deque()
    Q.append([y, x])
    vis[y][x] = 1
    while Q:
        y, x = Q.popleft()
        if y == end[0] and x == end[1]:
            return vis[y][x] - 2
        # 4방향 탐색
        for d in range(4):
            ny, nx = y, x
            # 모든 거리
            i = 0
            while 0 <= ny < H and 0 <= nx < W:
                if board[ny][nx] == "*": break
                if not vis[ny][nx]:
                    vis[ny][nx] = vis[y][x] + 1
                    Q.append([ny, nx])
                i += 1
                ny, nx = y + dy[d] * i, x + dx[d] * i

print(bfs(start[0], start[1]))