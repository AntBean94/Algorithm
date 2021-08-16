# 23강 이분 매칭 (Bipartite Matching) 예제

'''
예제

3 3 5
1 1
1 2
1 3
2 1
3 2

'''

import sys
input = sys.stdin.readline

# 초기값 세팅
S, N, M = map(int, input().split())
visit = [False] * (N + 1)
occupy = [0] * (N + 1)
graph = [[] for _ in range(S + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# 매칭에 성공한 경우 True, 실패한 경우 False 반환
def dfs(x):
    # 연결된 모든 노드에 대해서 점유 시도
    for i in range(len(graph[x])):
        y = graph[x][i]
        # 이미 처리된 노드(재귀 내에서)는 생략
        if visit[y]: continue
        visit[y] = True
        # 점유 노드가 없거나, 이미 점유한 노드가 다른곳으로 이동 가능하다면
        if occupy[y] == 0 or dfs(y):
            occupy[y] = x
            return True
    return False

cnt = 0
# 모든 출발 노드에 대해서 반복
for i in range(1, S + 1):
    # 도착 노드 방문여부 초기화
    for j in range(N + 1):
        visit[j] = False
    if dfs(i): cnt += 1

print(f'{cnt}개의 매칭이 이루어졌습니다.')
for i in range(1, len(occupy)):
    print(f'{i} -> {occupy[i]}')
        
