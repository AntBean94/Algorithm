# BOJ 14500 테트로미노

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

max_total = 0
# 시계방향 회전
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def check(map, x, y, k, total, d):
    global max_total
    if k == 3:
        if total > max_total:
            max_total = total
        return
    # 3방향 탐색
    for i in range(3):
        # 반대방향 탈출조건
        if i == 0 and d == 2 or i == 2 and d == 0:
            continue
        x += dx[i]
        y += dy[i]
        if 0 <= x < M and 0 <= y < N:
            val = map[y][x]
            check(map, x, y, k+1, total + val, i)
        x -= dx[i]
        y -= dy[i]

def check_bump(map, x, y):
    global max_total
    total = 0
    base = map[y][x]
    for i in range(4):
        sub_total = base
        for j in range(4):
            if i != j:
                if 0 <= x + dx[j] < M and 0 <= y + dy[j] < N:
                    sub_total += map[y+dy[j]][x+dx[j]]
                else:
                    break
        if sub_total > total:
            total = sub_total
    if total > max_total:
        max_total = total
    
for i in range(N):
    for j in range(M):
        check(map, j, i, 0, map[i][j], 5)
        check_bump(map, j, i)

print(max_total)