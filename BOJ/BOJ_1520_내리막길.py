# BOJ 1520 내리막 길 

'''
bfs + 우선순위 큐(최대 힙)

방문했던 기록이 있으면 방문 값에 자신의 값을 누적(이후 중복탐색 x)
'''

import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    vis[y][x] = 1
    Q = []
    heapq.heappush(Q, [-board[y][x], y, x])
    while Q:
        h, y, x = heapq.heappop(Q)
        h *= -1
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < M:
                nh = board[ny][nx]
                if nh < h:
                    # case 1. 방문 기록이 없을 때(큐에 넣는다.)
                    if not vis[ny][nx]: 
                        heapq.heappush(Q, [-nh, ny, nx])
                    # case 2. 방문 기록이 있다면 방문 값만 추가
                    vis[ny][nx] += vis[y][x]

vis = [[0] * M for _ in range(N)]
bfs(0, 0)
print(vis[N-1][M-1])