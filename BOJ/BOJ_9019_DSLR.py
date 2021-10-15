# BOJ 9019 DSLR

'''
1234

3412

DSLR에 따라 수정 BFS
각 명령어는 큐에 함께 저장
수정한 값 방문체크(집합 활용)
'''

from collections import deque

def trans(x:int):
    x = str(x)
    l = len(x)
    x = '0' * (4-l) + x
    return x

def bfs(a, b):
    a = trans(a)
    b = trans(b)
    vis = set()
    vis.add(a)
    Q = deque()
    Q.append([a, ""])
    while Q:
        a, route = Q.popleft()
        if a == b:
            return route
        for i in range(4):
            # D
            if i == 0:
                new_a = trans((int(a) * 2) % 10000) 
                new_route = route + 'D'
            elif i == 1:
                new_a = trans((int(a) - 1) % 10000)
                new_route = route + 'S'
            elif i == 2:
                new_a = a[1:] + a[0]
                new_route = route + 'L'
            else:
                new_a = a[3] + a[:3]
                new_route = route + 'R'
            if new_a not in vis:
                vis.add(new_a)
                Q.append([new_a, new_route])
    return

T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))