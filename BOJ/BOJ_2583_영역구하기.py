# BOJ 2583 영역 구하기

from collections import deque

N, M, K = map(int, input().split())
P = [[0] * M for _ in range(N)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            P[i][j] = 1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    result = 0
    Q = deque()
    Q.append([y, x])
    P[y][x] = 1
    while Q:
        y, x = Q.popleft()
        result += 1
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < M:
                if not P[ny][nx]:
                    P[ny][nx] = 1
                    Q.append([ny, nx])
    return result

cnt = 0
arr = []
for i in range(N):
    for j in range(M):
        if not P[i][j]:
            cnt += 1
            arr.append(bfs(i, j))
print(cnt)
print(*sorted(arr))