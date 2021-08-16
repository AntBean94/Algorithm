# BOJ 2188 축사 배정

'''
이분매칭
'''

import sys
input = sys.stdin.readline

# 주어진 정보(소, 축사)
N, M = map(int, input().split())
graph = [[0]]
for i in range(N):
    info = list(map(int, input().split()))
    graph.append(info[1:])

# 초기값 세팅(축사 정보)
shed = [0] * (M + 1)

# 이분 매칭 알고리즘
def bipartite(x):
    for i in range(len(graph[x])):
        y = graph[x][i]
        if visit[y]:
            continue
        visit[y] = True
        if shed[y] == 0 or bipartite(shed[y]):
            shed[y] = x
            return True
    return False

ans = 0
# 이분 매칭 실행
for i in range(1, N + 1):
    # 방문 정보 초기화
    visit = [False] * (M + 1)
    if bipartite(i):
        ans += 1

print(ans)
