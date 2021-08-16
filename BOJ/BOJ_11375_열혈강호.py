# BOJ 11375 열혈 강호

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0]]
for i in range(N):
    info = list(map(int, input().split()))
    graph.append(info[1:])

task = [0] * (M + 1)

def bipartite(x):
    for y in graph[x]:
        if visit[y]:
            continue
        visit[y] = True
        if task[y] == 0 or bipartite(task[y]):
            task[y] = x
            return True
    return False

ans = 0
for i in range(1, N + 1):
    visit = [False] * (M + 1)
    if bipartite(i):
        ans += 1
print(ans)