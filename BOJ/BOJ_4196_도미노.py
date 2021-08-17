# BOJ 4196 도미노

'''
위상정렬 + 강한결합요소 
'''

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(x):
    global id, id2
    visit[x] = id
    id += 1
    stack.append(x)
    parent = visit[x]
    for y in graph[x]:
        if visit[y] == 0: parent = min(parent, dfs(y))
        elif not finish[y]: parent = min(parent, visit[y])
    if parent == visit[x]:
        while True:
            t = stack.pop()
            finish[t] = 1
            hashing[t] = id2
            if t == x:
                id2 += 1
                break
    return parent


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    graph = [list() for _ in range(N + 1)]
    arr = []
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        arr.append([a, b])
    start = []

    visit = [0] * (N + 1)
    finish = [0] * (N + 1)
    stack = []
    id = 1
    id2 = 1
    hashing = {}
    for i in range(1, N + 1):
        if not visit[i]:
            dfs(i)

    indegree = [0] * id2

    for i in arr:
        if hashing[i[0]] != hashing[i[1]]:
            indegree[hashing[i[1]]] += 1
    ans = 0
    for i in indegree[1:]:
        if i == 0:
            ans += 1
    print(ans)