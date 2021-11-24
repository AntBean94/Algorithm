# BOJ 13023 ABCDE

'''
그래프

양방향이므로 위상정렬 불가능

모든 노드에 대해서?
2,000 * 2,000 = 4,000,000

dfs

'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list() for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    if vis[x] == 5:
        print(1)
        exit()
    for y in graph[x]:
        if not vis[y]:
            vis[y] = vis[x] + 1
            dfs(y)
            vis[y] = 0

for i in range(N):
    vis = [0] * N
    vis[i] = 1
    dfs(i)
print(0)