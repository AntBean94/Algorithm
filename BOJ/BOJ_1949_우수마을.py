# BOJ 1949 우수 마을

'''
1. 마을들은 트리구조
2. 양방향
3. 모든 마을은 연결되어있음
4. 직접 길로 연결되어 있을 때, 인접

우수마을 선정 조건
1. '우수 마을'로 선정된 마을 주민 수의 총 합을 최대로 해야 함
2. '우수 마을'끼리는 서로 인접할 수 없다.
3. '우수 마을'로 선정되지 못한 마을이라도 하나 이상의 인접한 
    '우수 마을'이 있어야 한다.

점화식
DP[root][T] = sum(DP[branch][F]) + W
DP[root][F] = sum(max(DP[branch]))
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10001)

N = int(input())
W = [0] + list(map(int, input().split()))
# 인접 정보 입력
graph = [list() for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 방문기록, DP 테이블
vis = [0] * (N + 1)
DP = [[0, 0] for _ in range(N + 1)]

def dfs(x):
    # 방문 처리
    vis[x] = 1
    for y in graph[x]:
        # 종료 조건
        if vis[y]: continue
        dfs(y)
        # case 1. not '우수 마을'
        DP[x][0] += max(DP[y])
        # case 2. '우수 마을'
        DP[x][1] += DP[y][0]
    # 우수마을 선정
    DP[x][1] += W[x]
    return

dfs(1)
print(max(DP[1]))