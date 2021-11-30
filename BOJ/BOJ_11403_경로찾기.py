# BOJ 11403 경로 찾기

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] + graph[k][j] > 1:
                graph[i][j] = 1
print()
for i in graph:
    print(*i)
