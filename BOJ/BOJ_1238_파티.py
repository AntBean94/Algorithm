# BOJ 1238 파티

'''
모든 마을의 갯수 1000

1. 모든 마을을 대상으로 다익스트라 = N * N * logN (시간초과)

2. x에서 두번
x -> 1, 2, 3, 4, ..., N (정방향)
x <- 1, 2, 3, 4, ..., N (역방향)
'''
import heapq
import sys
input = sys.stdin.readline
INF = 1000000000

N, M, X = map(int, input().split())
# 정방향, 역방향 그래프 정보 입력
post_graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    post_graph[a].append([b, c])
    reverse_graph[b].append([a, c])

# 정방향, 역방향 그래프 거리 정보 초기화
post_D = [INF] * (N + 1)
reverse_D = [INF] * (N + 1)

def dijkstra(graph, dist, start):
    Q = []
    heapq.heappush(Q, [0, start])
    dist[start] = 0
    while Q:
        cost, now = heapq.heappop(Q)
        for nxt, nxt_cost in graph[now]:
            new_cost = cost + nxt_cost
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(Q, [new_cost, nxt])

dijkstra(post_graph, post_D, X)
dijkstra(reverse_graph, reverse_D, X)
ans = max([i + j for i, j in zip(post_D[1:], reverse_D[1:])])
print(ans)