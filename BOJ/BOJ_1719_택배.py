# BOJ 1719 택배

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = 100000000
graph = [[INF] * (N + 1) for _ in range(1 + N)]
route = [['-'] * (N + 1) for _ in range(1 + N)]
for i in range(1, N + 1):
    graph[i][i] = 0
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    route[a][b] = b
    route[b][a] = a

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                route[i][j] = route[i][k]

for r in route[1:]:
    print(*r[1:])