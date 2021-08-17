# BOJ 3977 축구 전술

'''
강한결합요소 + 위상정렬
'''

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

# dfs 함수
def dfs(x):
    global id, id2
    visit[x] = id
    id += 1
    stack.append(x)
    parent = visit[x]
    # dfs탐색을 하며 부모를 변경
    for y in graph[x]:
        if visit[y] == 0: parent = min(parent, dfs(y))
        elif not finish[y]: parent = min(parent, visit[y])
    # 부모가 자신과 같다면 스택에 쌓인값을 뽑아낸다.
    if parent == visit[x]:
        scc = []
        while True:
            t = stack.pop()
            scc.append(t)
            finish[t] = True
            group[t] = id2
            # 자신을 만날때까지 뽑아내면 scc 구성완료
            if t == x:
                # 그룹 체크용 id값
                id2 += 1
                break
        SCC.append(scc)
    return parent

# 데이터 입력
T = int(input())
for tc in range(T):
    if tc: input()
    N, M = map(int, input().split())
    graph = [list() for _ in range(N)]
    arr = []
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        arr.append([a, b])
    
    # dfs 탐색에 필요한 값
    visit = [0] * N
    finish = [False] * N
    stack = []
    group = {}
    SCC = []
    id, id2 = 1, 1
    for i in range(N):
        if visit[i] == 0:
            dfs(i)

    # 그룹별 진입차수 초기화
    indegree = [0] * id2
    for i in arr:
        if group[i[0]] != group[i[1]]:
            indegree[group[i[1]]] += 1
    
    # 진입차수가 0인 그룹 뽑기
    zero = []
    for i in range(1, id2):
        if indegree[i] == 0:
            zero.append(i)
    # 진입차수 0인 그룹이 1개라면 SCC 원소 출력
    if len(zero) == 1:
        for i in sorted(SCC[zero[0]-1]):
            print(i)
    # 1개가 아니면 Confused 출력
    else:
        print("Confused")
    print()
    