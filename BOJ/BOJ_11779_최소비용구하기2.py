# BOJ 11779 최소비용 구하기 2

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
        if dist[cur] < dist_c: continue
        for nxt, dist_n in graph[cur]:
            cost = dist_c + dist_n
            if cost < dist[nxt]:
                route[nxt] = cur
                dist[nxt] = cost
                heapq.heappush(q, (cost, nxt))

route = [i for i in range(N + 1)]
dist = [INF] * (N + 1)
dijkstra(S)
print(dist[E])
result = [E]
pre = E
now = route[E]
while pre != now:
    result.append(now)
    pre = now
    now = route[pre]
print(len(result))
print(*result[::-1])
