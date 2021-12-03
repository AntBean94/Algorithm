# BOJ 10026 적록색약

'''
적록색약, 일반 상황 구분한 bfs
'''

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = [list(i for i in input().rstrip()) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x, t):
    char = board[y][x]
    Q = deque()
    Q.append([y, x])
    vis[y][x] = 1
    while Q:
        y, x = Q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                nxt = board[ny][nx]
                # 일반인(0)인 경우
                if not t:
                    if nxt == char and not vis[ny][nx]:
                        vis[ny][nx] = 1
                        Q.append([ny, nx])
                # 적록색약(1)인 경우
                else:
                    if not vis[ny][nx]:
                        if char == "R" or char == "G":
                            if nxt == "R" or nxt == "G":
                                vis[ny][nx] = 1
                                Q.append([ny, nx])
                        else:
                            if nxt == "B":
                                vis[ny][nx] = 1
                                Q.append([ny, nx])

ans = [0, 0]
for t in range(2):
    cnt = 0
    vis = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not vis[i][j]:
                cnt += 1
                bfs(i, j, t)
    ans[t] = cnt
print(*ans)