# Softeer 차세대 지능형 교통시스템

import sys
input = sys.stdin.readline

'''

절차
현재 방향
    통과 가능한 신호 확인
        통과한 신호에서 뻗을 수 있는 방향

중복방향 체크 함수...
가도 되는지 여부는 visit 배열에 거리 체크
1. 방문 기록이 없으면 통과
2. 기록이 있지만 해당 거리일때 신호가 무었이었는지를 
    체크해서 갈수 없는 방향이면 진출
- 같은 포인트라도 들어간 시간대가 다르다면 이동할 수 있는 지점이 다르므로 통과
- 
'''

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 신호별 출발방향
PS = [0, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2]

DIR = [
    [],
    [0, 1, 2], [0, 1, 3], [0, 2, 3],
    [1, 2, 3], [0, 1], [0, 3], 
    [2, 3], [1, 2], [1, 2],
    [0, 1], [0, 3], [2, 3],
]

N, T = map(int, input().split())
''' SIG ex)
[]
[[], [2, 6, 12, 9], [7, 1, 11, 6], [6, 3, 5, 11]]
[[], [1, 1, 12, 9], [3, 11, 8, 2], [1, 7, 11, 9]]
[[], [4, 6, 2, 3], [2, 4, 2, 4], [6, 9, 2, 6]]
'''
SIG = [list() for _ in range(N + 1)]
for i in range(1, N+1):
    SIG[i].append([])
    for j in range(N):
        dir = list(map(int, input().split()))
        SIG[i].append(dir)

vis = [list([] for _ in range(N + 1)) for _ in range(N + 1)]

# dfs 함수
def dfs(y, x, t, di):
    # 방문기록
    vis[y][x].append([t % 4, di])
    # 이번 신호에 막히면 리턴
    if di != PS[SIG[y][x][t % 4]] or t == T: return
    # 갈 수 있는 방향 (0, 1, 3 등)
    for do in DIR[SIG[y][x][t % 4]]:
        ny = y + dy[do]
        nx = x + dx[do]
        # 진출이 가능하다면
        if 0 < ny <= N and 0 < nx <= N:
            # 방문체크(방문기록이 있다면 생략)
            nt = t + 1
            # 방문 기록이 있는데 통과 못한 케이스
            # 방문 기록이 있는데 통과 할 수 있는케이스
            if [nt % 4, do] in vis[ny][nx]: continue
            # 방문기록이 없다면
            else:
                dfs(ny, nx, nt, do)
        
dfs(1, 1, 0, 0)
ans = 0
for i in range(N + 1):
    for j in range(N + 1):
        if vis[i][j]:
            ans += 1

print(ans)
