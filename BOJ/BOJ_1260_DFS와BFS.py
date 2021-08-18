# BOJ 1260 DFS와 BFS

import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [list() for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

def dfs(x):
    visit[x] = True
    print(x, end=" ")
    for y in graph[x]:
        if not visit[y]:
            dfs(y)

def bfs(x):
    visit[x] = True
    Q = deque()
    Q.append(x)
    while Q:
        t = Q.popleft()
        print(t, end=" ")
        for y in graph[t]:
            if not visit[y]:
                Q.append(y)
                visit[y] = True

visit = [False] * (N + 1)
# dfs 실행
dfs(V)
print()

visit = [False] * (N + 1)
bfs(V)