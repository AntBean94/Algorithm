# BOJ 20040 사이클 게임

'''
1. 입력으로 주어진 값의 부모를 확인
2. 부모가 다르다면 큰값의 부모를 작은값으로 수정
3. 부모가 같다면 사이클 형성 
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [i for i in range(N + 1)]

def get_parent(graph, x):
    if graph[x] == x: return x
    graph[x] = get_parent(graph, graph[x])
    return graph[x]

def union_parent(graph, x, y):
    x = get_parent(graph, x)
    y = get_parent(graph, y)
    if x <= y: graph[y] = x
    else: graph[x] = y

def find_parent(graph, x, y):
    x = get_parent(graph, x)
    y = get_parent(graph, y)
    if x == y: return True
    else: return False

check = True
for i in range(M):
    a, b = map(int, input().split())
    if check:
        if find_parent(graph, a, b):
            print(i + 1)
            check = False
        else: union_parent(graph, a, b)
if check:
    print(0)