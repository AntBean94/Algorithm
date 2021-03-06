# BOJ 1504 특정한 최단 경로


'''
1, A, B, N

1번 정점과 N번 정점 사이의 최소거리
=> 1번 정점과 A, B의 최소거리를 구하고
=> N번 정점과 A, B의 최소거리를 구한다.
=> A, B의 최소거리를 구한다.

각 최소거리를 조합해 1부터 N정점까지의 최소거리를 구한다.
'''

import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
INF = 1000000000
graph = [[] for _ in range(N + 1)]
distance = [[INF] * (N + 1) for _ in range(3)]
# print(distance)
for i in range(E):
    a, b, d = map(int, input().split())
    graph[a].append([b, d])
    graph[b].append([a, d])
A, B = map(int, input().split())

def dijkstra(start, k):
    q = []
    heapq.heappush(q, (0, start))
    distance[k][start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[k][now] < dist: continue
        for nxt, di in graph[now]:
            cost = dist + di
            if cost < distance[k][nxt]:
                distance[k][nxt] = cost
                heapq.heappush(q, (cost, nxt))

arr = [1, A, N]
for i in range(3):
    start = arr[i]
    dijkstra(start, i)
for d in distance:
    print(d[1:])
# 정답 출력
# 1, 3, 2, 4 vs 1, 2, 3, 4
ans_A = distance[0][A] + distance[1][B] + distance[2][B]
ans_B = distance[0][B] + distance[1][B] + distance[2][A]
if min(ans_A, ans_B) >= 1000000000:
    print(-1)
else:
    print(min(ans_A, ans_B))