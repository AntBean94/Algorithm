# BOJ 1671 상어의 저녁식사

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
shark = [[]]
for _ in range(N):
    a, b, c = map(int, input().split())
    shark.append([a, b, c])
graph = [list() for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if shark[j][0] == shark[i][0] and shark[j][1] == shark[i][1] and shark[j][2] == shark[i][2]:
            graph[j].append(i)
        elif shark[j][0] >= shark[i][0] and shark[j][1] >= shark[i][1] and shark[j][2] >= shark[i][2]:
            graph[j].append(i)
        elif shark[j][0] <= shark[i][0] and shark[j][1] <= shark[i][1] and shark[j][2] <= shark[i][2]:
            graph[i].append(j)

S = [0] * (N + 1)
def bipartite(x):
    for y in graph[x]:
        if visit[y]:
            continue
        visit[y] = True
        if S[y] == 0 or bipartite(S[y]):
            S[y] = x
            return True
    return False

ans = 0
for k in range(2):
    for i in range(1, N + 1):
        visit = [False] * (N + 1)
        if bipartite(i):
            ans += 1
print(N - ans)



