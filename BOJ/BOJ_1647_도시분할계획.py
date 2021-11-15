# BOJ 1647 도시 분할 계획

'''
최단거리?
유니온 파인드?
크루스칼?

길을 하나뺀 크루스칼
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
node = [i for i in range(N + 1)]
route = [list(map(int, input().split())) for _ in range(M)]
route.sort(key=lambda x: x[2])

def get_parent(node, x):
    if x == node[x]: return x
    node[x] = get_parent(node, node[x])
    return node[x]

def union_parent(node, x, y):
    x = get_parent(node, x)
    y = get_parent(node, y) 
    if y < x: node[x] = y
    else: node[y] = x

def find_parent(node, x, y):
    x = get_parent(node, x)
    y = get_parent(node, y)
    if y != x: return False
    else: return True

cnt = 0
cost = 0
for a, b, c in route:
    if not find_parent(node, a, b):
        union_parent(node, a, b)
        cnt += 1
        cost += c
    if cnt == N - 2: break
print(cost)