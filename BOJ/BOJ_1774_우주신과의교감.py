# BOJ 1774 우주신과의 교감

'''
방법
1. 연결된 간선의 가중치를 0으로 만드는 방법

2. 연결된 간선의 그래프를 미리 기록해두는 방법
'''

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# 노드의 좌표
nodes = []
route = []
for i in range(1, N + 1):
    a, b = map(int, input().split())
    for j, val in enumerate(nodes):
        route.append([i, j + 1, (a - val[0]) ** 2 + (b - val[1]) ** 2])
    nodes.append([a, b])
route.sort(key=lambda x: x[2])

def get_parent(graph, x):
    if x == graph[x]: return x
    graph[x] = get_parent(graph, graph[x])
    return graph[x]

def union_parent(graph, x, y):
    x = get_parent(graph, x)
    y = get_parent(graph, y)
    if x < y: graph[y] = x
    else: graph[x] = y

def find_parent(graph, x, y):
    x = get_parent(graph, x)
    y = get_parent(graph, y)
    if x == y: return True
    else: return False

# 기 연결된 통로
graph = [i for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    union_parent(graph, a, b)

# 새로 연결해야 할 통로
cnt = M
ans = 0
for a, b, r in route:
    if not find_parent(graph, a, b):
        union_parent(graph, a, b)
        ans += r ** (1 / 2)
        cnt += 1
    if cnt == N - 1: break
print("%0.2f" %ans)