# 22강 네트워크 플로우 (Network Flow) 예제

'''
네트워크 플로우 예제 입력값

start(시작), end(종료)
V(노드 갯수), E(간선 갯수)
간선 정보
노드 노드 용량

1 6
6 10
1 2 12
1 4 11
2 3 6
2 4 3
2 5 5
2 6 9
3 6 8
4 5 9
5 3 3
5 6 4

'''
from collections import deque 

INF = 1000000000

start, end = map(int, input().split())
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
C = [[0] * (V+1) for _ in range(V+1)]
F = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    C[a][b] = c
result = 0

def maxFlow(start, end):
    global result
    while True:
        visit = [-1] * (V+1)
        Q = deque()
        Q.append(start)
        while Q:
            x = Q.popleft()
            for y in graph[x]:
                # 방문기록이 없고 용량이 남은경우
                if C[x][y] - F[x][y] > 0 and visit[y] == -1:
                    Q.append(y)
                    visit[y] = x
                    if y == end: break
        
        # 모든 경로를 다찾아서 더이상 도달할 수 없는경우(while 탈출)
        if visit[end] == -1: break
        # 경로의 유량
        flow = INF
        # 가능한 최소유량을 거꾸로 탐색해간다.
        pre = end
        while pre != start:
           now = visit[pre]
           flow = min(flow, C[now][pre] - F[now][pre])
           pre = now
        # 최소유량을 더한다.
        pre = end
        while pre != start:
            now = visit[pre]
            F[now][pre] += flow
            F[pre][now] -= flow
            pre = now
        result += flow
        
maxFlow(start, end)
print(result)