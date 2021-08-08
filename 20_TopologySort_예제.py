# 20강 위상 정렬 (Topology Sort) 예제

from collections import deque

'''
입력 예제

노드의 갯수, 간선의 갯수
간선정보

7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

'''

# 노드, 간선 갯수 정보 입력
v, e = map(int, input().split())
# 진입 차수 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담을 연결리스트 초기화
graph = [[] for _ in range(v + 1)]

# 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상정렬 함수
def topology_sort():
    result = []
    Q = deque()
    
    # 진입차수 0인 값을 찾아 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            Q.append(i)
    
    # 반복
    while Q:
        now = Q.popleft()
        result.append(now)
        for next in graph[now]:
            # 진입차수를 감소 => 간선 제거
            indegree[next] -= 1
            # 진입차수가 0이라면 Q에 삽입
            if indegree[next] == 0:
                Q.append(next)
            
    print(*result)

topology_sort()