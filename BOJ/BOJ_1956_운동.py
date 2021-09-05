# BOJ 1956 운동

'''
일방통행

사이클을 이루는 도로의 길이의 최소합을 구하시오.
두 마을을 왕복하는 경우도 사이클에 포함

모든 정점에 대해 다익스트라?
'''

import sys, heapq
input = sys.stdin.readline

INF = 100000000
V, E = map(int, input().split())
dist = [[INF] * (V + 1) for _ in range(V + 1)]
graph = [[] for _ in range(V + 1)]
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start][start] = 0
    while q:
        dc, cur = heapq.heappop(q)
        if dc > dist[start][cur]: continue
        for nxt, dn in graph[cur]:
            cost = dist[start][cur] + dn
            if nxt == start and dist[start][start] == 0:
                dist[start][nxt] = cost
                continue
            if cost < dist[start][nxt] and cost < ans:
                dist[start][nxt] = cost
                heapq.heappush(q, (cost, nxt))
    return dist[start][start]

ans = 1000000000
for i in range(V):
    st = i + 1
    result = dijkstra(st)
    if result and result < ans:
        ans = result
if ans >= 1000000000:
    print(-1)
else:
    print(ans)