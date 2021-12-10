# BOJ 2533 사회망 서비스(SNS)

'''
N = 1,000,000

필요한 얼리 어답터의 최소를 구하자

그래프만 주어짐

[내가 얼리어답터가 아닐때, 내가 얼리어답터일때]
[
    [3, 3], [2, 1], [0, 1], [2, 1], [0, 1], [0, 1], [0, 1], [0, 1]
]

내가 얼리어답터라면 내 친구는 (얼리, 낫얼리)
내가 얼리어답터가 아니면 내친구는 (얼리)

즉, 한명이라도 얼리어답터가 아니면 무조건 얼리어답터
전부 얼리어답터면 걔네 수만 더하면 됨
즉 나는
0, 1로 시작

0 = 얼리어답터가 아니므로 내 자식들이 얼리어답터인경우의 갯수를 모두 더한경우

1 = 얼리어답터가 맞으므로 내자식들이 얼리어답터이거나, 얼리어답터가 아닌경우를 모두 더한경우(최솟값)
'''

import sys
sys.setrecursionlimit(1000001)
input = sys.stdin.readline

N = int(input())
graph = [list() for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    vis[x] = 1
    for y in graph[x]:
        if not vis[y]:
            dfs(y)
            # case 1. not early adaptor
            DP[x][0] += DP[y][1]
            # case 2. early adaptor
            DP[x][1] += min(DP[y][0], DP[y][1])

vis = [0] * (N + 1)
DP = [[0, 1] for _ in range(N + 1)]
dfs(1)
print(min(DP[1]))