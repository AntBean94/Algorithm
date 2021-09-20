# BOJ 17142 연구소 3

'''
모든 경우의 수: 252가지

완탐 + 백트래킹

50 * 50 = 2500
bfs

불가능한 경우 -1출력
'''
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 바이러스 위치 기록
virus = []
emp_cnt = 0
for i in range(N):
    for j in range(N):
        tmp = board[i][j]
        if tmp == 2: virus.append([i, j])
        elif tmp == 0: emp_cnt += 1

# 모든 조합 뽑기
result = []
tmp = []
def comb(arr, i):
    global result
    if len(tmp) == M: 
        result.append(list(tmp))
        return
    for j in range(i, len(arr)):
        tmp.append(arr[j])
        comb(arr, j + 1)
        tmp.pop()

comb([i for i in range(len(virus))], 0)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
# bfs
def bfs(start, emp_cnt):
    dist = 0
    Q = deque()
    # 방문 체크
    for y, x in start:
        Q.append([y, x])
        vis[y][x] = 1
    while Q:
        y, x = Q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if not vis[ny][nx] and not board[ny][nx] == 1:
                    Q.append([ny, nx])
                    vis[ny][nx] = vis[y][x] + 1
                    if board[ny][nx] == 0:
                        emp_cnt -= 1
                        if vis[ny][nx] > dist: dist = vis[ny][nx]
                        if emp_cnt == 0: return dist
                    if vis[ny][nx] > ans: return 1000000
    if emp_cnt > 0: return 1000000
    else: return dist

ans = 1000000
# 모든 조합에 대해 bfs
for case in result:
    vis = [[0] * N for _ in range(N)]
    start = []
    for c in case:
        start.append(virus[c])
    dist = bfs(start, emp_cnt)
    if dist < ans: 
        ans = dist

if ans == 1000000: print(-1)
elif ans == 0: print(0)
else: print(ans - 1)