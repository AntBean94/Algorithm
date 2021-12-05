# BOJ 15681 트리와 쿼리

'''
100,000

그래프를 트리로 변환?
=> dfs 활용

dfs로 변환하는 과정에서 노드의 갯수를 세서 테이블에 저장
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

N, R, Q = map(int, input().split())
graph = [list() for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs 알고리즘
def dfs(x):
    vis[x] = 1
    tmp = 0
    for y in graph[x]:
        if not vis[y]:
           tmp += dfs(y)
    DP[x] = tmp + 1
    return DP[x]

DP = [0] * (N + 1)
vis = [0] * (N + 1)
dfs(R)

# 쿼리
for i in range(Q):
    print(DP[int(input())])