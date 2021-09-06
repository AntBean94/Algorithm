# BOJ 1916 최소비용 구하기

import sys, heapq
input = sys.stdin.readline

INF = 1000000000
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

S, E = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        dist_c, cur = heapq.heappop(q)
        if dist_c > dist[cur]: continue
        for nxt, dist_n in graph[cur]:
            cost = dist_c + dist_n
            if cost < dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(q, (cost, nxt))

dist = [INF] * (N + 1)
dijkstra(S)
print(dist[E])