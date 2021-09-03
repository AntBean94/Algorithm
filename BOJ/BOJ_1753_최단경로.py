# BOJ 1753 최단경로

import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = 100000000
graph = [[] for _ in range(V + 1)]
for i in range(E):
    s, e, d = map(int, input().split())
    graph[s].append([e, d])
distance = [INF] * (V + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist_a, now = heapq.heappop(q)
        if distance[now] < dist_a:
            continue
        for nxt, dist_b in graph[now]:
            cost = distance[now] + dist_b
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))

dijkstra(K)
for d in distance[1:]:
    if d != 100000000: print(d)
    else: print('INF')