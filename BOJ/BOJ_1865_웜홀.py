# BOJ 1865 웜홀

'''
N개의 노드
M개의 간선(방향 X)
W개의 웜홀(방향 O)

*웜홀 
- 시작 위치에서 도착 위치로 가는 하나의 경로
- 도착시 시작을 했을때보다 시간이 뒤로 간다.
음의 간선 => 벨만-포드?
'''

import sys
input = sys.stdin.readline
INF = 1000000000

def bellman_ford(route, start):
    dist = [INF] * (N + 1)
    dist[start] = 0
    for i in range(N):
        for j in range(2 * M + W):
            now = route[j][0]
            nxt = route[j][1]
            time = route[j][2]
            if dist[now] + time < dist[nxt]:
                dist[nxt] = dist[now] + time
                if i == N - 1:
                    return True
    return False

T = int(input())
for tc in range(T):
    N, M, W = map(int, input().split())
    route = []
    # 도로 정보, 웜홀 정보 입력(M + W)
    for i in range(M):
        a, b, c = map(int, input().split())
        route.append([a, b, c])
        route.append([b, a, c])
    for i in range(W):
        a, b, c = map(int, input().split())
        route.append([a, b, -c])
    # 벨만-포드
    check = False
    if bellman_ford(route, 1):
        check = True
    if check: print("YES")
    else: print("NO")