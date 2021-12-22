# BOJ 2468 안전 영역

from collections import deque
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x, n):
    Q = deque()
    Q.append([y, x])
    vis[y][x] = 1
    while Q:
        y, x = Q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if not vis[ny][nx] and A[ny][nx] > n:
                    Q.append([ny, nx])
                    vis[ny][nx] = 1
    return

H = set([0])
for i in range(N):
    for j in range(N):
        H.add(A[i][j])

ans = 0
for h in H:
    cnt = 0
    vis = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not vis[i][j] and A[i][j] > h:
                bfs(i, j, h)
                cnt += 1
    if cnt > ans: ans = cnt
print(ans)