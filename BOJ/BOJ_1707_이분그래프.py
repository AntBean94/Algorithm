# BOJ 1707 이분 그래프

'''
1. 이분 그래프 정의

그래프 T = (V, E) 와 자연수 k가 주어졌다고 하자. 
만약 V가 다음과 같은 조건을 만족시키는 집합의 분할
V = V1 U V2 U ... U Vk 
을 가질 수 있다면, T를 k분 그래프라고 한다.

=> 즉, 그래프의 정점의 집합을 2등분 했을 때 각 집합의
각 정점들이 서로 인접하지 않으면 2분 그래프라 함

2. 이분그래프 확인방법
계층별로 정점에 칼라를 칠했을 때, 같은 칼라를 가진
정점이 인접했다면 이분그래프가 아님
'''

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    vis[x] = 1
    Q = deque()
    Q.append(x)
    while Q:
        x = Q.popleft()
        for y in graph[x]:
            if not vis[y]:
                # 방문한적이 없다면 x의 반대값
                vis[y] = -vis[x]
                Q.append(y)
            else:
                # 방문한적 있는데 칼라가 같다면 NO
                if vis[y] == vis[x]:
                    return False
    return True

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    vis = [0] * (V + 1)
    ans = 'YES'
    for i in range(1, V + 1):
        if not vis[i]:
            if not bfs(i):
                ans = 'NO'
                break
    print(ans)