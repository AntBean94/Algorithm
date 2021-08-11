# 21강 강한 결합 요소 (Strongly Connected Component) 예제

'''
강한 결합요소를 추출해보자

-- 예제 --
11 14
1 2
2 3
3 1
4 2
4 5
5 7
7 6
6 5
8 5
8 9
9 10
10 11
11 3
11 8

'''

id = 1
MAX = 10001
d = [0] * MAX
finished = [False] * MAX
stack = []
SCC = []

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for i in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(x):
    global id
    d[x] = id
    id += 1

    stack.append(x)
    parent = d[x]
    for i in range(len(graph[x])):
        y = graph[x][i]
        # 방문하지 않았다면
        if d[y] == 0: parent = min(parent, dfs(y))
        # 진행중이라면
        elif not finished[y]: parent = min(parent, d[y])
    # 부모 노드가 자기 자신인 경우
    if parent == d[x]:
        scc = []
        while True:
            t = stack.pop()
            scc.append(t)
            finished[t] = True
            if t == x:
                break
        SCC.append(scc)
    # 부모 반환
    return parent

for i in range(1, V):
    if d[i] == 0:
        dfs(i)

# 출력
print(f"SCC의 갯수는: {len(SCC)}")
for i in range(len(SCC)):
    print(f"{i}번째 SCC: ", end="")
    for j in SCC[i]:
        print(j, end=" ")
    print()