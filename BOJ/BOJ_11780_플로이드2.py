# BOJ 11780 플로이드 2

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 100000000
graph = [[INF] * (N + 1) for _ in range(N + 1)]
route = [[False] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0
for i in range(M):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c
        route[a][b] = b

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                route[i][j] = route[i][k]

# 비용 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == 100000000:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
# 경로 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == 100000000:
            print(0)
        else:
            cnt = 0
            path = []
            now, end = i, j
            while now != end:
                cnt += 1
                path.append(now)
                now = route[now][end]
            if cnt:
                cnt += 1
                path.append(now)
            print(cnt, *path)