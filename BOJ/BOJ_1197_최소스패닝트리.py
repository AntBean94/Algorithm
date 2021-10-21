# BOJ 1197 최소 스패닝 트리

'''
1. 간선 가중치 기준으로 정렬
2. 간선을 이루는 두 정점이 같은 트리에 있는지 확인
3. 없다면 연결
'''

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [i for i in range(V + 1)]

def get_parent(graph, x):
    if graph[x] == x: return x
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

route = []
for i in range(E):
    route.append(list(map(int, input().split())))
route.sort(key=lambda x: x[2])

# 간선 연결
cnt = 0
ans = 0
for a, b, c in route:
    if not find_parent(graph, a, b):
        union_parent(graph, a, b)
        cnt += 1
        ans += c
    if cnt == V - 1: break
print(ans)