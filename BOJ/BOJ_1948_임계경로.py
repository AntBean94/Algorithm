# BOJ 1948 임계경로

from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [list() for _ in range(N + 1)]
indegree = [0] * (N + 1)
time = dict()
dp_table = [0] * (N + 1)
route = [[i] for i in range(N + 1)]
for i in range(M):
    a, b, t = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    time[f'{a}{b}'] = t

start, end = map(int, input().split())
Q = deque()
Q.append(start)
# 반복문 시작
while Q:
    x = Q.popleft()
    for y in graph[x]:
        if indegree[y]:
            cost = time[f'{x}{y}']
            if dp_table[x] + cost > dp_table[y]:
                dp_table[y] = dp_table[x] + cost
                route[y] = [x]
            elif dp_table[x] + cost == dp_table[y]:
                route[y].append(x)
            indegree[y] -= 1
            if indegree[y] == 0:
                Q.append(y)
# 마지막 도착시간
print(dp_table[end])
# 쉬지않고 달리는 도로 갯수
cnt = 0
def dfs(r):
    global cnt
    for i in route[r]:
        if i != r and time[f'{i}{r}']:
            cnt += 1
            time[f'{i}{r}'] = 0
            dfs(i)
        else:
            return
dfs(end)
print(cnt)