# BOJ 14938 서강그라운드

import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
INF = 100000
graph = [[INF] * (N + 1) for _ in range(N + 1)]
items = [0] + list(map(int, input().split()))
for i in range(N):
    graph[i][i] = 0
for i in range(R):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 최대 아이템 갯수 체크
ans = 0
for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N + 1):
        if graph[i][j] <= M:
            cnt += items[j]
    if cnt > ans:
        ans = cnt
print(ans)