# BOJ 1005 ACM Craft

'''
위상정렬
'''

import heapq
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    indegree = [0] * N
    graph = {}
    for i in range(K):
        x, y = map(int, input().split())
        x, y = x - 1, y - 1
        indegree[y] += 1
        if not x in graph:
            graph[x] = list([y])
        else: graph[x].append(y)
    W = int(input()) - 1
    vis = [0] * N
    Q = []
    now = 0
    ans = 0
    while True:
        # 1. 진입차수가 0인 건물 확인 및 우선순위큐 삽입
        for i in range(N):
            if indegree[i] == 0 and not vis[i]:
                # 시간, 건물번호
                heapq.heappush(Q, [D[i] + now, i])
                vis[i] = 1
        # 2. 우선순위 큐에서 가장 짧은 건물 뽑기
        now, num = heapq.heappop(Q)
        if num == W:
            ans = now
            break
        # 3. 진입차수 0으로 만들기
        if num in graph:
            for i in graph[num]:
                indegree[i] -= 1
    print(ans)