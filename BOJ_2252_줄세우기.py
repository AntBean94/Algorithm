# BOJ 2252 줄 세우기

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 진입차수
indegree = [0] * (N + 1)
graph = [list() for _ in range(N + 1)]
# 그래프에 담기
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

Q = deque()
# 진입차수가 0인 지점 찾아서 큐에 넣기
for i in range(1, N + 1):
    if indegree[i] == 0:
        Q.append(i)

# 반복문을 돌며 위상정렬을 실시한다.
while Q:
    x = Q.popleft()
    print(x, end=" ")
    for y in graph[x]:
        if indegree[y]:
            indegree[y] -= 1
            if indegree[y] == 0:
                Q.append(y)
