# BOJ 10217 KCM Travel

'''
M원 이하로 사용하면서 도착할 수 있는 최단거리

인천: 1, LA: N

u, v, c, d

거리정보
단순히 최단 거리에 따른 비용정보만 계산하면 안됨
전체 경로에 따른 비용정보를 가지고 있어야 한다.
'''

import sys
from collections import deque
input = sys.stdin.readline

def dijkstra(start):
    dist = [[INF] * (M + 1) for _ in range(N + 1)]
    q = deque()
    q.append((0, 0, start))
    dist[start][0] = 0
    while q:
        cost_c, dist_c, cur = q.popleft()
        if dist_c > dist[cur][cost_c]: continue
        for nxt, cost_n, dist_n in graph[cur]:
            dist_t = dist_c + dist_n
            cost_t = cost_c + cost_n
            if cost_t > M: continue
            if dist_t >= dist[nxt][cost_t]: continue
            if dist_t < dist[nxt][0]:
                dist[nxt][0] = dist_t
            for i in range(cost_t, M + 1):
                if dist_t < dist[nxt][i]: dist[nxt][i] = dist_t
                else: break
            q.append((cost_t, dist_t, nxt))
    return dist[-1][0]

INF = 1000000000
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for i in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append([v, c, d])

    result = dijkstra(1)
    if result >= INF: print('Poor KCM')
    else: print(result)