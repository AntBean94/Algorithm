# BOJ 2213 트리의 독립집합

'''
정점의 가중치가 주어진 경우
최대 독립 집합(독립 집합에 속한 정점의 가중치의 합)을 구해보자.

독립 집합(Independent Set): 정점의 부분 집합 S에 속한 모든 
정점쌍이 서로 인접하지 않는 경우

예제
1 - 2 - 3 - 4 - 5
    |
    6 - 7

=> 트리 구조이기 때문에 bottom-up 방식의 접근 가능

점화식
DP[parent][T] = sum(DP[child][F]) + W[parent]
DP[parent][F] += max(DP[child][T], DP[child][F])

경로
집합으로 관리
'''

import sys
input = sys.stdin.readline

N = int(input())
# 정점의 가중치
W = [0] + list(map(int, input().split()))
# 간선 정보
graph = [list() for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

DP = [[[0, set()], [0, set()]] for _ in range(N + 1)]
vis = [0] * (N + 1)

def dfs(x):
    vis[x] = 1
    for y in graph[x]:
        if vis[y]: continue
        dfs(y)
        DP[x][0][0] += max(DP[y])[0]
        DP[x][0][1] = DP[x][0][1] | max(DP[y])[1]
        DP[x][1][0] += DP[y][0][0]
        DP[x][1][1] = DP[x][1][1] | DP[y][0][1]
    DP[x][1][0] += W[x]
    DP[x][1][1].add(x)
    return

dfs(1)
ans = max(DP[1])
print(ans[0])
print(*sorted(ans[1]))