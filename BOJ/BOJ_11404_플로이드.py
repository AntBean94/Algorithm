# BOJ 11404 플로이드

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 1000000000
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0
for i in range(M):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == 1000000000:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()