# BOJ 4803 트리

import sys
input = sys.stdin.readline

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

tc = 0
while True:
    tc += 1
    N, M = map(int, input().split())
    if not N: break
    graph = [i for i in range(N + 1)]
    tree = set()
    no_tree = set()
    for i in range(M):
        a, b = map(int, input().split())
        if find_parent(graph, a, b):
            no_tree.add(graph[a])
        else:
            # 순환 그래프 포함여부 확인
            if graph[a] in no_tree: no_tree.add(graph[b])
            if graph[b] in no_tree: no_tree.add(graph[a])
            union_parent(graph, a, b)
    
    # 루트 노드 확인
    for i in range(1, N + 1):
        tree.add(get_parent(graph, i))
    cnt = len(tree - no_tree)

    # 정답 출력
    if cnt > 1: print(f'Case {tc}: A forest of {cnt} trees.')
    elif cnt > 0: print(f'Case {tc}: There is one tree.')
    else: print(f'Case {tc}: No trees.')