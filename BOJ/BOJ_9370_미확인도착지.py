# BOJ 9370 미확인 도착지

'''
dijkstra 알고리즘

경로 기록(거리 초기화시)
'''

import heapq
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split())
    INF = 1000000000
    graph = [[] for _ in range(N + 1)]
    distance = [[INF] * (N + 1) for _ in range(3)]
    for i in range(M):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])

    # 목적지 후보
    candidate = []
    for i in range(T):
        candidate.append(int(input()))

    # 다익스트라
    def dijkstra(start, k):
        q = []
        heapq.heappush(q, (0, start))
        distance[k][start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[k][now]: continue
            for nxt, dist_n in graph[now]:
                cost = dist + dist_n
                if cost < distance[k][nxt]:
                    distance[k][nxt] = cost
                    heapq.heappush(q, (cost, nxt))
    
    # S, G, H 정점을 기준으로 다익스트라 
    arr = [S, G, H]
    for i in range(3):
        dijkstra(arr[i], i)

    # 냄새 경로가 최단거리에 포함되는지 확인
    result = []
    for i in candidate:
        g = distance[0][G] + distance[1][H] + distance[2][i]
        h = distance[0][H] + distance[2][G] + distance[1][i]
        if distance[0][i] == min(g, h):
            heapq.heappush(result, i)
    print(*sorted(result))