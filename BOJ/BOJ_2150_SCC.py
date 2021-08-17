# BOJ 2150 Strongly Connected Component

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [list() for _ in range(E)]
for i in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

finish = [False] * (V + 1)
visit = [0] * (V + 1)
stack = []
SCC = []
id = 1

def dfs(x):
    global id
    visit[x] = id
    id += 1

    parent = visit[x]
    stack.append(x)
    for y in graph[x]:
        # 방문전이면 dfs
        if visit[y] == 0: parent = min(parent, dfs(y))
        # 처리중이면
        elif not finish[y]: parent = min(parent, visit[y])
    # 부모가 나와 같다면
    if parent == visit[x]:
        scc = []
        while True:
            t = stack.pop()
            scc.append(t)
            finish[t] = True
            if x == t:
                break
        SCC.append(scc)
    
    return parent

for i in range(1, V + 1):
    if visit[i] == 0:
        dfs(i)

ans = len(SCC)
for i in range(ans):
    SCC[i].sort()
SCC.sort(key=lambda x: x[0])

print(ans)
for i in SCC:
    print(" ".join(map(str, i)) + " -1")

