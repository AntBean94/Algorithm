# Programmers 전력망을 둘로 나누기

from collections import deque

# 완전 탐색 + bfs
def bfs(graph, s, a, b, n):
    cnt = 0
    vis = [0] * (n + 1)
    Q = deque()
    Q.append(s)
    vis[s] = 1
    while Q:
        t = Q.popleft()
        cnt += 1
        for v in graph[t]:
            if not vis[v]:
                if (t == a and v == b) or (t == b and v == a): continue
                vis[v] = 1
                Q.append(v)
    return cnt
    
def solution(n, wires):
    answer = 10000
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    for a, b in wires:
        result = bfs(graph, 1, a, b, n)
        result = abs(result * 2 - n)
        if result < answer: answer = result   
    return answer