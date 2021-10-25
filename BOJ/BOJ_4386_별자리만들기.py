# BOJ 4386 별자리 만들기

'''
1. 모든 간선의 가중치 측정
2. 정렬
3. 연결(Kruskal)
'''

import sys
input = sys.stdin.readline

N = int(input())
line = []
points = []
# 1. 가중치 측정
for i in range(N):
    a, b = map(float, input().split())
    for idx, y, x in points:
        line.append([idx, i + 1, (y - a) ** 2 + (x - b) ** 2])
    points.append([i + 1, a, b])

# 2. 정렬
line.sort(key=lambda x: x[2])

# 3. 연결(Kruskal)
def get_parent(graph, x):
    if x == graph[x]: return x
    graph[x] = get_parent(graph, graph[x])
    return graph[x]

def union_parent(graph, y, x):
    y = get_parent(graph, y)
    x = get_parent(graph, x)
    if y < x: graph[x] = y
    else: graph[y] = x

def find_parent(graph, y, x):
    y = get_parent(graph, y)
    x = get_parent(graph, x)
    if y != x: return False
    else: return True

graph = [i for i in range(N + 1)]
cnt = 0
result = 0
for a, b, g in line:
    if not find_parent(graph, a, b):
        union_parent(graph, a, b)
        cnt += 1
        result += g ** (1 / 2)
    if cnt == N - 1: break
print(result)