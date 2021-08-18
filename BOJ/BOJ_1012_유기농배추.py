# BOJ 1012 유기농 배추

import sys
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    graph[y][x] = 0
    Q = []
    Q.append([y, x])
    while Q:
        ny, nx = Q.pop()
        for i in range(4):
            ty = ny + dy[i]
            tx = nx + dx[i]
            if 0 <= ty < N and 0 <= tx < M:
                if graph[ty][tx]:
                    graph[ty][tx] = 0
                    Q.append([ty, tx])

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    ans = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                ans += 1
                bfs(i, j)
                
    print(ans)