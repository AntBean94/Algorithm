# BOJ 11724 연결 요소의 개수

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list() for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

vis = [0] * (N + 1)

def bfs(x):
    Q = deque()
    Q.append(x)
    vis[x] = 1
    while Q:
        x = Q.popleft()
        for y in graph[x]:
            if not vis[y]:
                vis[y] = 1
                Q.append(y)

ans = 0
for i in range(1, N + 1):
    if not vis[i]:
        bfs(i)
        ans += 1
print(ans)