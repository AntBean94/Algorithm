# BOJ 1967 트리의 지름

'''
트리의 지름 구하는 방법

임의의 한 노드 x에서 가장 먼 노드 a와 거리를 구한다.
a노드에서 가장 먼 노드 b와 거리를 구한다.

지름 = (a - b) 의 거리
'''

import sys
input = sys.stdin.readline

N = int(input())
graph = [list() for _ in range(N + 1)]
for i in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def dfs(x):
    vis = [0] * (N + 1)
    Q = []
    Q.append(x)
    vis[x] = 1
    max_node = 0
    max_lth = 1
    while Q:
        x = Q.pop()
        for y, yw in graph[x]:
            if not vis[y]:
                vis[y] = vis[x] + yw
                Q.append(y)
                if vis[y] > max_lth:
                    max_lth = vis[y]
                    max_node = y
    return max_node, max_lth - 1

a, lth = dfs(1)
b, lth = dfs(a)
print(lth)