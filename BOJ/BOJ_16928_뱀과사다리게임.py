# BOJ 16928 뱀과 사다리 게임

'''
사다리와 뱀은 각각 최대 15개

1번은 2, 3, 4, 5, 6, 7 로 이동가능한 그래프

bfs로 풀기
'''

from collections import deque

N, M = map(int, input().split())
graph = [list(range(i+1, min(i+7, 101))) for i in range(101)]
event = {i:i for i in range(101)}
# 사다리 정보 입력
for i in range(N):
    x, y = map(int, input().split())
    event[x] = y
# 뱀 정보 입력
for i in range(M):
    u, v = map(int, input().split())
    event[u] = v

def bfs(x):
    Q = deque()
    Q.append(x)
    vis[x] = 1
    while Q:
        x = Q.popleft()
        if x == 100: return vis[x] - 1
        for y in graph[x]:
            y = event[y]
            if not vis[y]:
                vis[y] = vis[x] + 1
                Q.append(y)
    return

vis = [0] * 101
print(bfs(1))