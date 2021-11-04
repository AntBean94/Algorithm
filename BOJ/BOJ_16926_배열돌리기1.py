# BOJ 16926 배열 돌리기 1

import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def make_arr(vis, k):
    tmp = []
    y, x, d = k, k, 0
    tmp.append([y, x])
    vis[y][x] = 1
    while d < 4:
        ny, nx = y + dy[d], x + dx[d]
        if i <= ny < N - i and i <= nx < M - i and not vis[ny][nx]:
            vis[ny][nx] = 1
            tmp.append([ny, nx])
            y, x = ny, nx
        else: d += 1
    return tmp

trans_arr = {}
vis = [[0] * M for _ in range(N)]
m = min(N, M) // 2
for i in range(m):
    key = 2 * (N + M - 4 * i - 2)
    trans_arr[key] = make_arr(vis, i)

new_arr = [[0] * M for _ in range(N)]
for key, value in trans_arr.items():
    r = R % key  # 이동할 거리
    for i in range(key):
        y, x = value[i]
        ny, nx = value[(i + r) % key]
        new_arr[ny][nx] = arr[y][x]

# 출력
for a in new_arr:
    print(*a)