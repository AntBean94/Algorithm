# BOJ 1167 트리의 지름

'''
트리의 지름: 임의의 두 점 사이의 거리 중 가장 긴 것을 의미

1 - 3
    |
2 - 4 - 5

지름: 11

1. 트리에서 임의의 정점 x를 잡는다.
2. 정점 x에서 가장 먼 정점 y를 찾는다.
3. 정점 y에서 가장 먼 정점 z를 찾는다.

지름: 정점 y에서 정점 z까지의 거리

'''

import sys
input = sys.stdin.readline

V = int(input())
tree = [list() for _ in range(V + 1)]
for i in range(V):
    info = list(map(int, input().split()))
    v = info[0]
    for j in range(1, len(info), 2):
        if info[j] == -1: break
        tree[v].append([info[j], info[j+1]])

def dfs(x):
    vis = [0] * (V + 1)
    m, m_val = 0, 0
    Q = []
    Q.append(x)
    vis[x] = 1
    while Q:
        x = Q.pop()
        for y, d in tree[x]:
            if not vis[y]:
                Q.append(y)
                vis[y] = vis[x] + d
                if vis[y] > m_val: m, m_val = y, vis[y]
    return m, m_val - 1

m, m_val = dfs(1)
n, n_val = dfs(m)
print(n_val)