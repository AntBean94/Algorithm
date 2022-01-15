# BOJ 2644 촌수계산

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [list() for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x, a):
    vis = [0] * (N + 1)
    Q = deque()
    Q.append(x)
    vis[x] = 1
    while Q:
        x = Q.popleft()
        if x == a:
            return vis[x] - 1
        for y in graph[x]:
            if not vis[y]:
                vis[y] = vis[x] + 1
                Q.append(y)
    return -1

print(bfs(A, B))