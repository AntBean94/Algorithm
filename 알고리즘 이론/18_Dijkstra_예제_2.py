# 18강 다익스트라 알고리즘 (Dijkstra Algorithm) 예제 (2)

# 힙 구조 활용 - O(NlogN)

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9) # 10억

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 시작 노드 입력
start = int(input())
# 노드 정보 리스트
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)

# 간선 정보 입력
for i in range(m):
    s, e, d = map(int, input().split())
    graph[s].append([e, d])

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단 거리 노드정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# dijkstra 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1, n+1):
    # 도달 할 수 없는 경우 INFINITY 출력
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])

'''인풋 에제
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
