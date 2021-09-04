# BOJ 11657 타임머신

import sys
input = sys.stdin.readline

INF = 1000000000
N, M = map(int, input().split())
route = []
for i in range(M):
    route.append(list(map(int, input().split())))

# 시작 노드 설정
start = 1
# 최단 거리 배열 초기화
dist = [INF] * (N + 1)

# 벨만-포드 알고리즘
def bellman_ford(start):
    dist[start] = 0
    # N번의 라운드
    for i in range(N):
        # 모든 간선을 순환
        for j in range(M):
            now = route[j][0]
            nxt = route[j][1]
            cost = route[j][2]
            # 최단거리 배열 갱신이 가능한 경우
            if dist[now] != INF and dist[now] + cost < dist[nxt]:
                dist[nxt] = dist[now] + cost
                if i == N - 1:
                    return True
    return False

if bellman_ford(start):
    print(-1)
else:
    for d in dist[2:]:
        if d < 1000000000:
            print(d)
        else:
            print(-1)